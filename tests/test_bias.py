import math,unittest
import pipeline as p
class BiasTests(unittest.TestCase):
 def test_offsets_match_independent_training_grid_oracle(self):
  c=dict(dt_seconds=.1,resistance_grid=[1,2],compliance_grid=[1,3]);flow=[20,40,80];observed=[76,74,75];before=list(observed)
  result=p.calibration_bias_probe(flow,observed,c)
  self.assertEqual([x['offset_mmHg'] for x in result['cases']],[-1,0,1])
  for row in result['cases']:
   oracle=min((math.sqrt(sum((a-b-row['offset_mmHg'])**2 for a,b in zip(p.simulate(r,cc,flow,.1),observed))/3),r,cc) for r in [1,2] for cc in [1,3])
   self.assertEqual((row['estimated_R'],row['estimated_C']),oracle[1:]);self.assertAlmostEqual(row['calibration_rmse_mmHg'],oracle[0])
  self.assertEqual(observed,before)
 def test_invalid_calibration_observations_remain_rejected(self):
  with self.assertRaises(ValueError):p.calibration_bias_probe([1],[float('nan')],dict(dt_seconds=.1,resistance_grid=[1],compliance_grid=[1]))
