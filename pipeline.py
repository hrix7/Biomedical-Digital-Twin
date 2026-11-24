"""Deterministic experiment runner. Python standard library only."""
import argparse
import csv
import hashlib
import io
import json
import math
from pathlib import Path
import random
import statistics

ROOT = Path(__file__).resolve().parent

def digest(data):
    return hashlib.sha256(data).hexdigest()

def encode(obj):
    return (json.dumps(obj, indent=2, sort_keys=True, allow_nan=False) + "\n").encode()

def table(rows):
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, lineterminator="\n")
    writer.writerows(rows)
    return stream.getvalue().encode()

def mean(xs):
    return statistics.mean(xs)

def finite_product(*values):
    # Exponent-scaled multiplication avoids intermediate overflow AND underflow.
    mantissa=1.0;exponent=0
    for value in values:
        if not math.isfinite(value):raise ValueError('finite factors required')
        fraction,power=math.frexp(value);mantissa*=fraction;exponent+=power
    try:result=math.ldexp(mantissa,exponent)
    except OverflowError:raise ValueError('product must be representable') from None
    if not math.isfinite(result):raise ValueError('product must be finite')
    return result

def simulate(resistance, compliance, inflow, dt, initial=80):
    if any(not math.isfinite(x) or x <= 0 for x in (resistance, compliance, dt)):
        raise ValueError('R, C and dt must be finite and positive')
    if not math.isfinite(initial):
        raise ValueError('initial pressure must be finite')
    time_constant = resistance * compliance
    if not math.isfinite(time_constant) or time_constant <= 0:
        raise ValueError('R*C must be representable as a finite positive time constant')
    # Exact piecewise-constant solution of C dP/dt = Q - P/R.
    exponent = -dt / time_constant
    decay = math.exp(exponent)
    # expm1 retains the inflow contribution when exp(exponent) rounds to 1.
    inflow_gain = -math.expm1(exponent)
    pressure = initial
    values = []
    for flow in inflow:
        if not math.isfinite(flow):
            raise ValueError('inflow samples must be finite')
        pressure = pressure*decay + finite_product(resistance,flow,inflow_gain)
        if not math.isfinite(pressure):
            raise ValueError('pressure overflowed; use representable inputs')
        values.append(pressure)
    return values

def rmse(a,b):
    if len(a) != len(b) or not a:
        raise ValueError('equal nonempty vectors required')
    if any(not math.isfinite(v) for v in list(a)+list(b)):
        raise ValueError('loss vectors must be finite')
    errors=[abs(x-y) for x,y in zip(a,b)]
    if any(not math.isfinite(v) for v in errors):
        raise ValueError('loss differences must be representable')
    scale=max(errors)
    return scale*math.sqrt(mean([(v/scale)**2 for v in errors])) if scale else 0.0

def calibration_grid(inflow, observed, config):
    if not inflow or len(inflow)!=len(observed) or any(not math.isfinite(v) for v in list(inflow)+list(observed)):
        raise ValueError('finite equal nonempty calibration vectors required')
    if not config['resistance_grid'] or not config['compliance_grid']:
        raise ValueError('nonempty parameter grids required')
    candidates = [(rmse(simulate(r,c,inflow,config['dt_seconds']),observed),r,c)
                  for r in config['resistance_grid'] for c in config['compliance_grid']]
    return sorted(candidates)

def calibration_profiles(grid):
    """Discrete nuisance-parameter minimization, not confidence intervals."""
    return {key:[dict(value=v,minimum_rmse_mmHg=min(row[0] for row in grid if row[index]==v)) for v in sorted({row[index] for row in grid})] for key,index in [('R',1),('C',2)]}

def calibrate(inflow, observed, config):
    return calibration_grid(inflow,observed,config)[0]

def forcing_step_probe(resistance,compliance,dt,phase_samples=50):
    if type(phase_samples) is not int or phase_samples<1:
        raise ValueError('positive integer phase_samples required')
    if not math.isfinite(dt) or dt<=0 or not math.isfinite(2*phase_samples*dt):
        raise ValueError('finite positive representable probe duration required')
    inflow=[0]*phase_samples+[100]*phase_samples
    predicted=simulate(resistance,compliance,inflow,dt)
    tau=resistance*compliance;split=phase_samples*dt;middle=80*math.exp(-split/tau)
    reference=[80*math.exp(-(i+1)*dt/tau) if i<phase_samples else 100*resistance+(middle-100*resistance)*math.exp(-((i+1)*dt-split)/tau) for i in range(2*phase_samples)]
    return dict(initial_pressure_mmHg=80,flow_before_mL_s=0,flow_after_mL_s=100,switch_time_seconds=split,phase_samples=phase_samples,max_abs_error_mmHg=max(abs(a-b) for a,b in zip(predicted,reference)),samples=[dict(time_seconds=(i+1)*dt,flow_mL_s=q,pressure_mmHg=p,closed_form_mmHg=r) for i,(q,p,r) in enumerate(zip(inflow,predicted,reference))],interpretation='Separate deterministic zero-to-constant-flow probe with an independent two-phase closed form; same ideal model, not physiological or patient validation.')

def ramp_pressure(time,resistance,compliance,initial=80,q0=20,slope=30):
    simulate(resistance,compliance,[],1,initial)  # shared parameter contract only
    if not math.isfinite(time) or time<0 or any(not math.isfinite(v) for v in (q0,slope)):
        raise ValueError('finite nonnegative time and finite forcing required')
    tau=resistance*compliance;gain=-math.expm1(-time/tau)
    x=time/tau
    # Stable integral of ramp forcing: avoid subtracting nearly equal times.
    lag=time-tau*gain if abs(x)>=1e-3 else time*x*(.5+x*(-1/6+x*(1/24+x*(-1/120+x/720))))
    result=initial*math.exp(-x)+resistance*(q0*gain+slope*lag)
    if not math.isfinite(result):raise ValueError('representable analytic pressure required')
    return result

def ramp_forcing_probe(resistance,compliance,duration=2,resolutions=(25,50,100)):
    if not math.isfinite(duration) or duration<=0 or not isinstance(resolutions,(tuple,list)) or not resolutions or any(type(n) is not int or n<1 for n in resolutions) or len(set(resolutions))!=len(resolutions):
        raise ValueError('positive duration and unique positive sample counts required')
    reference=ramp_pressure(duration,resistance,compliance);cases=[]
    for count in resolutions:
        dt=duration/count;flow=[20+30*i*dt for i in range(count)]
        endpoint=simulate(resistance,compliance,flow,dt)[-1]
        cases.append(dict(samples=count,dt_seconds=dt,endpoint_mmHg=endpoint,analytic_endpoint_mmHg=reference,absolute_endpoint_error_mmHg=abs(endpoint-reference)))
    return dict(duration_seconds=duration,q0_mL_s=20,slope_mL_s2=30,cases=cases,interpretation='Separate linear-ramp forcing Q(t)=20+30t with independent continuous-forcing closed form. Left-endpoint piecewise-constant flow approximates this ramp; errors should converge with timestep refinement. This is same-model numerical validation, not patient/physiological validation or calibration uncertainty.')

def validate_config(config):
    if not isinstance(config,dict):raise ValueError('configuration object required')
    if type(config.get('seed')) is not int:raise ValueError('integer seed required')
    if type(config.get('samples')) is not int or config['samples']<2 or type(config.get('calibration_samples')) is not int or not 1<=config['calibration_samples']<config['samples']:
        raise ValueError('nonempty calibration and forward holdout required')
    positive=lambda v:not isinstance(v,bool) and isinstance(v,(int,float)) and math.isfinite(v) and v>0
    for key in ('dt_seconds','true_R','true_C','baseline_R','baseline_C'):
        if not positive(config.get(key)):raise ValueError(key+' must be finite and positive')
    noise=config.get('observation_noise_sd_mmHg')
    if isinstance(noise,bool) or not isinstance(noise,(int,float)) or not math.isfinite(noise) or noise<0:raise ValueError('finite nonnegative observation noise required')
    for key in ('resistance_grid','compliance_grid'):
        grid=config.get(key)
        if not isinstance(grid,list) or not grid or any(not positive(v) for v in grid) or len(set(grid))!=len(grid):raise ValueError('unique finite positive parameter grids required')
    if not math.isfinite(config['samples']*config['dt_seconds']) or not math.isfinite(100*config['dt_seconds']):raise ValueError('representable experiment and probe durations required')
    for r,c in [(config['true_R'],config['true_C']),(config['baseline_R'],config['baseline_C'])]+[(r,c) for r in config['resistance_grid'] for c in config['compliance_grid']]:
        if not math.isfinite(r*c) or r*c<=0:raise ValueError('representable positive time constants required')

def run(config):
    validate_config(config)
    rng = random.Random(config['seed'])
    dt = config['dt_seconds']
    inflow = [max(0, 80 + 70*math.sin(2*math.pi*i*dt)) for i in range(config['samples'])]
    clean = simulate(config['true_R'],config['true_C'],inflow,dt)
    observed = [p+rng.gauss(0,config['observation_noise_sd_mmHg']) for p in clean]
    cut = config['calibration_samples']
    grid=calibration_grid(inflow[:cut],observed[:cut],config)
    loss,r,c = grid[0]
    predicted = simulate(r,c,inflow,dt)
    baseline = simulate(config['baseline_R'],config['baseline_C'],inflow,dt)
    sensitivity = {f'R_multiplier_{m}':rmse(simulate(r*m,c,inflow,dt)[cut:],clean[cut:]) for m in (.8,1,1.2)}
    rows = [['sample','time_seconds','flow_mL_per_second','clean_mmHg','observed_mmHg','estimated_mmHg','flow_interval_start_seconds']]
    rows.extend([i,format((i+1)*dt,'.12g'),format(q,'.12g'),format(p,'.12g'),format(o,'.12g'),format(e,'.12g'),format(i*dt,'.12g')]
                for i,(q,p,o,e) in enumerate(zip(inflow,clean,observed,predicted)))
    return rows, dict(ramp_forcing_probe=ramp_forcing_probe(config['true_R'],config['true_C']),forcing_step_probe=forcing_step_probe(config['true_R'],config['true_C'],dt),time_convention='time_seconds labels post-step pressure at (i+1)*dt; each flow value applies on [flow_interval_start_seconds, time_seconds). Initial pressure at t=0 is not an exported observation.',estimated_R=r,estimated_C=c,calibration_rmse_mmHg=loss,
                      holdout_rmse_vs_observed_mmHg=rmse(predicted[cut:],observed[cut:]),
                      holdout_rmse_vs_synthetic_truth_mmHg=rmse(predicted[cut:],clean[cut:]),
                      baseline_holdout_rmse_mmHg=rmse(baseline[cut:],clean[cut:]),
                      sensitivity=sensitivity,
                      calibration_grid=[dict(rmse_mmHg=e,R=rr,C=cc) for e,rr,cc in grid],
                      calibration_profiles=calibration_profiles(grid),
                      calibration_runner_up_gap_mmHg=grid[1][0]-loss if len(grid)>1 else None,
                      calibration_best_on_grid_boundary=dict(R=r in (min(config['resistance_grid']),max(config['resistance_grid'])),C=c in (min(config['compliance_grid']),max(config['compliance_grid']))) ,
                      grid_interpretation='Calibration-only loss surface, not a confidence region or proof of identifiability; holdout values do not select parameters.',
                      interpretation='Synthetic parameter recovery within the same generating model; no patient-specific or clinical validation.')

def experiment():
    config = json.loads((ROOT / 'config.json').read_text())
    rows, metrics = run(config)
    data = table(rows)
    result = dict(schema_version=1, project=ROOT.name, data_kind='synthetic',
                  config=config, config_sha256=digest((ROOT/'config.json').read_bytes()),
                  source_sha256=digest(Path(__file__).read_bytes()),
                  data_sha256=digest(data), metrics=metrics)
    result_bytes = encode(result)
    report = ('# Verified synthetic experiment\n\n'
              'Educational engineering benchmark. No clinical validity is claimed.\n\n'
              'Generated from `config.json` by `pipeline.py`. Metrics are computed, never hand-entered.\n\n'
              '```json\n' + json.dumps(metrics, indent=2, sort_keys=True, allow_nan=False) + '\n```\n\n'
              'Result SHA-256: `' + digest(result_bytes) + '`\n').encode()
    return {'data.csv':data,'results.json':result_bytes,'report.md':report}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--verify',action='store_true',help='Recompute and compare every result byte; do not overwrite')
    parser.add_argument('--output',type=Path,default=ROOT/'results')
    args = parser.parse_args()
    files = experiment()
    manifest = {name:digest(data) for name,data in files.items()}
    files['manifest.json'] = encode(manifest)
    if args.verify:
        for name,data in files.items():
            path = args.output/name
            if not path.exists() or path.read_bytes() != data:
                raise SystemExit('Verification failed: '+name)
        print('Verified: deterministic recomputation and all artifact checksums match')
    else:
        args.output.mkdir(parents=True,exist_ok=True)
        for name,data in files.items():
            (args.output/name).write_bytes(data)
        print('Generated synthetic data, measured results, report and checksums')

if __name__ == '__main__':
    main()
