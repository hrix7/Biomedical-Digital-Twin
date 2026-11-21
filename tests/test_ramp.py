import math,unittest
import pipeline as p
class RampTests(unittest.TestCase):
 def test_initial_zero_slope_and_independent_formula(self):
  self.assertEqual(p.ramp_pressure(0,2,3),80)
  self.assertAlmostEqual(p.ramp_pressure(2,2,3,q0=0,slope=0),80*math.exp(-2/6),places=12)
  t=2;R=2;C=3;tau=R*C
  expected=R*(20+30*(t-tau))+(80-R*(20-30*tau))*math.exp(-t/tau)
  self.assertAlmostEqual(p.ramp_pressure(t,R,C),expected,places=12)
 def test_first_order_refinement_measured_without_tolerance_relaxation(self):
  rows=p.ramp_forcing_probe(1.2,1.5)['cases'];errors=[r['absolute_endpoint_error_mmHg'] for r in rows]
  self.assertTrue(errors[0]>errors[1]>errors[2]>0)
  self.assertTrue(1.8<errors[0]/errors[1]<2.2);self.assertTrue(1.8<errors[1]/errors[2]<2.2)
 def test_invalid_inputs(self):
  for duration,resolutions in [(0,(25,)),(2,()),(2,(True,)),(2,(25,25))]:
   with self.assertRaises(ValueError):p.ramp_forcing_probe(1,1,duration,resolutions)
  with self.assertRaises(ValueError):p.ramp_pressure(-1,1,1)

 def test_tiny_ramp_response_against_high_precision_integral(self):
  from decimal import Decimal,localcontext
  for t in (1e-12,1e-8,1e-4,.000999,.001001):
   with localcontext() as ctx:
    ctx.prec=70;d=Decimal(str(t));expected=float(d-(1-(-d).exp()))
   actual=p.ramp_pressure(t,1,1,initial=0,q0=0,slope=1)
   self.assertTrue(math.isclose(actual,expected,rel_tol=1e-12), (t,actual,expected))
