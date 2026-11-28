import unittest,math
import pipeline as p
class Residuals(unittest.TestCase):
 def test_independent_centered_products(self):
  r=p.calibration_residuals([2,3,5],[1,1,1])
  # Errors [1,2,4], centered [-4/3,-1/3,5/3].
  self.assertAlmostEqual(r['mean_observed_minus_predicted_mmHg'],7/3)
  self.assertAlmostEqual(r['rmse_mmHg'],math.sqrt(7))
  self.assertAlmostEqual(r['centered_lag1_ratio'],-1/42)
  self.assertEqual(r['samples'],3)
 def test_constant_and_large_scale(self):
  self.assertIsNone(p.calibration_residuals([2,2],[1,1])['centered_lag1_ratio'])
  self.assertEqual(p.calibration_residuals([0],[0])['rmse_mmHg'],0)
  self.assertTrue(math.isfinite(p.calibration_residuals([1e300,2e300],[0,0])['rmse_mmHg']))
 def test_invalid_inputs(self):
  for a,b in (([],[]),([1],[1,2]),([True],[0]),([float('nan')],[0]),([1e308],[-1e308])):
   with self.assertRaises(ValueError):p.calibration_residuals(a,b)
