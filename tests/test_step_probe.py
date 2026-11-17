import unittest,math
import pipeline as p
class StepProbeTests(unittest.TestCase):
 def test_independent_phase_endpoints_and_switch(self):
  r=p.forcing_step_probe(2,3,.1,10);rows=r['samples']
  self.assertEqual(len(rows),20);self.assertEqual(rows[9]['flow_mL_s'],0);self.assertEqual(rows[10]['flow_mL_s'],100)
  middle=80*math.exp(-1/6);end=200+(middle-200)*math.exp(-1/6)
  self.assertAlmostEqual(rows[9]['pressure_mmHg'],middle,places=10);self.assertAlmostEqual(rows[-1]['pressure_mmHg'],end,places=10)
  self.assertLess(r['max_abs_error_mmHg'],1e-9)
 def test_invalid_phase_rejected(self):
  for n in (0,-1,True,1.5):
   with self.assertRaises(ValueError):p.forcing_step_probe(1,1,.02,n)

 def test_unrepresentable_export_time_rejected(self):
  with self.assertRaises(ValueError):p.forcing_step_probe(1,1,1e308)
