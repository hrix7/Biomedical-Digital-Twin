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
        pressure = pressure*decay + resistance*flow*inflow_gain
        if not math.isfinite(pressure):
            raise ValueError('pressure overflowed; use representable inputs')
        values.append(pressure)
    return values

def rmse(a,b):
    if len(a) != len(b) or not a:
        raise ValueError('equal nonempty vectors required')
    return math.sqrt(mean([(x-y)**2 for x,y in zip(a,b)]))

def calibration_grid(inflow, observed, config):
    candidates = [(rmse(simulate(r,c,inflow,config['dt_seconds']),observed),r,c)
                  for r in config['resistance_grid'] for c in config['compliance_grid']]
    return sorted(candidates)

def calibrate(inflow, observed, config):
    return calibration_grid(inflow,observed,config)[0]

def run(config):
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
    rows = [['sample','time_seconds','flow_mL_per_second','clean_mmHg','observed_mmHg','estimated_mmHg']]
    rows.extend([i,format(i*dt,'.12g'),format(q,'.12g'),format(p,'.12g'),format(o,'.12g'),format(e,'.12g')]
                for i,(q,p,o,e) in enumerate(zip(inflow,clean,observed,predicted)))
    return rows, dict(estimated_R=r,estimated_C=c,calibration_rmse_mmHg=loss,
                      holdout_rmse_vs_observed_mmHg=rmse(predicted[cut:],observed[cut:]),
                      holdout_rmse_vs_synthetic_truth_mmHg=rmse(predicted[cut:],clean[cut:]),
                      baseline_holdout_rmse_mmHg=rmse(baseline[cut:],clean[cut:]),
                      sensitivity=sensitivity,
                      calibration_grid=[dict(rmse_mmHg=e,R=rr,C=cc) for e,rr,cc in grid],
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
