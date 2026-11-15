import unittest,json,math
import pipeline as p
class TimeAlignmentTests(unittest.TestCase):
 def test_csv_times_label_post_step_observations_and_flow_intervals(self):
  c=json.loads((p.ROOT/'config.json').read_text());rows,metrics=p.run(c);dt=c['dt_seconds'];header=rows[0]
  self.assertEqual(header[-1],'flow_interval_start_seconds')
  self.assertAlmostEqual(float(rows[1][1]),dt);self.assertEqual(float(rows[1][-1]),0)
  self.assertAlmostEqual(float(rows[-1][1]),c['samples']*dt)
  for i,row in enumerate(rows[1:]):
   self.assertAlmostEqual(float(row[1])-(float(row[-1])),dt,places=10)
   self.assertEqual(int(row[0]),i)
  first_expected=c['true_R']*80+(80-c['true_R']*80)*math.exp(-dt/(c['true_R']*c['true_C']))
  self.assertAlmostEqual(float(rows[1][3]),first_expected,places=8)
  self.assertIn('post-step',metrics['time_convention'])
