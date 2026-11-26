import unittest
import pipeline as p
class ProfileContractTests(unittest.TestCase):
 def test_invalid_grids_fail_before_reporting_profiles(self):
  for grid in ([],None,[(float('nan'),1,1)],[(float('inf'),1,1)],[(-1,1,1)],[(0,0,1)],[(0,1,True)],[(0,1)],[(0,1,1),(2,1,1)]):
   with self.subTest(grid=grid):
    with self.assertRaises(ValueError):p.calibration_profiles(grid)
 def test_zero_loss_and_reordered_finite_grid_remain_valid(self):
  grid=[(0,1,2),(1,2,2)];r=p.calibration_profiles(grid)
  self.assertEqual(r,p.calibration_profiles(list(reversed(grid))))
  self.assertEqual(r['C'][0]['minimum_rmse_mmHg'],0)
