import unittest
import pipeline as p
class ProfileTests(unittest.TestCase):
 def test_hand_grid_nuisance_minimum_and_ties(self):
  grid=[(3,1,2),(1,1,4),(1,3,2),(5,3,4)]
  before=list(grid);r=p.calibration_profiles(grid)
  self.assertEqual(r,{'R':[{'value':1,'minimum_rmse_mmHg':1},{'value':3,'minimum_rmse_mmHg':1}],'C':[{'value':2,'minimum_rmse_mmHg':1},{'value':4,'minimum_rmse_mmHg':1}]})
  self.assertEqual(grid,before)
 def test_singleton_and_grid_permutation(self):
  grid=[(.2,2,3),(.4,4,3)]
  self.assertEqual(p.calibration_profiles(grid),p.calibration_profiles(list(reversed(grid))))
  self.assertEqual(len(p.calibration_profiles(grid)['C']),1)
