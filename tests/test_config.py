import json,unittest
from unittest.mock import patch
import pipeline as p
class ConfigTests(unittest.TestCase):
 def setUp(self):self.c=json.loads((p.ROOT/'config.json').read_text())
 def test_invalid_inputs_fail_before_simulation(self):
  changes=[('samples',1),('samples',True),('calibration_samples',0),('calibration_samples',600),('dt_seconds',0),('dt_seconds',1e308),('true_R',float('nan')),('baseline_C',True),('observation_noise_sd_mmHg',-1),('resistance_grid',[]),('resistance_grid',[1,1]),('compliance_grid',[float('inf')])]
  with patch.object(p,'simulate',side_effect=AssertionError('must validate first')) as sim:
   for key,value in changes:
    with self.subTest(key=key,value=value):
     with self.assertRaises(ValueError):p.run({**self.c,key:value})
   c=dict(self.c);del c['true_C']
   with self.assertRaises(ValueError):p.run(c)
   sim.assert_not_called()
 def test_minimum_duration_and_singleton_grid(self):
  c={**self.c,'samples':2,'calibration_samples':1,'resistance_grid':[1.2],'compliance_grid':[1.5],'observation_noise_sd_mmHg':0}
  rows,m=p.run(c);self.assertEqual(len(rows),3);self.assertIsNone(m['calibration_runner_up_gap_mmHg']);self.assertEqual(m['holdout_rmse_vs_synthetic_truth_mmHg'],0)
