import unittest,math
import pipeline as p
class LossContractTests(unittest.TestCase):
 def test_large_representable_rmse_does_not_square_overflow(self):
  self.assertTrue(math.isclose(p.rmse([1e200,-1e200],[0,0]),1e200,rel_tol=1e-14))
  self.assertEqual(p.rmse([0,0],[0,0]),0)
 def test_nonfinite_and_unrepresentable_errors_rejected(self):
  for a,b in [([float('nan')],[0]),([0],[float('inf')]),([1e308],[-1e308])]:
   with self.assertRaises(ValueError):p.rmse(a,b)
 def test_invalid_observations_cannot_select_a_grid_winner(self):
  cfg={'dt_seconds':.02,'resistance_grid':[1],'compliance_grid':[1]}
  for flow,obs in [([] ,[]),([1],[float('nan')]),([1,2],[1])]:
   with self.assertRaises(ValueError):p.calibration_grid(flow,obs,cfg)
  cfg['resistance_grid']=[]
  with self.assertRaises(ValueError):p.calibration_grid([1],[1],cfg)
