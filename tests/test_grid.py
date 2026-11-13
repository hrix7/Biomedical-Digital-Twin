import unittest
import pipeline as p
class GridTests(unittest.TestCase):
 def test_constant_equilibrium_exposes_compliance_tie(self):
  c={'dt_seconds':.02,'resistance_grid':[1,1.2],'compliance_grid':[1,2]}
  rows=p.calibration_grid([80]*20,[80]*20,c)
  self.assertEqual(len(rows),4);self.assertEqual(rows,sorted(rows));self.assertAlmostEqual(rows[0][0],0,places=10);self.assertAlmostEqual(rows[1][0],0,places=10)
  self.assertEqual({row[2] for row in rows if row[0]<1e-10},{1,2})
 def test_ranked_grid_matches_selected_calibration(self):
  c={'dt_seconds':.02,'resistance_grid':[.8,1.2],'compliance_grid':[1,1.5]}
  q=[20,100]*20;observed=p.simulate(1.2,1.5,q,.02)
  grid=p.calibration_grid(q,observed,c)
  self.assertEqual(grid[0],(0,1.2,1.5));self.assertEqual(p.calibrate(q,observed,c),grid[0])
