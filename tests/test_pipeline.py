import copy
import json
import math
from pathlib import Path
import random
import subprocess
import sys
import tempfile
import unittest
import pipeline as p

class Reproducibility(unittest.TestCase):
    def test_repeatable(self):
        self.assertEqual(p.experiment(), p.experiment())
    def test_all_metrics_finite(self):
        result = json.loads(p.experiment()['results.json'])
        def walk(x):
            if isinstance(x, float): self.assertTrue(math.isfinite(x))
            elif isinstance(x,dict):
                for v in x.values(): walk(v)
            elif isinstance(x,list):
                for v in x: walk(v)
        walk(result)
    def test_verifier_rejects_tampering(self):
        with tempfile.TemporaryDirectory() as d:
            cmd=[sys.executable,str(p.ROOT/'pipeline.py'),'--output',d]
            subprocess.run(cmd,check=True,capture_output=True)
            subprocess.run(cmd+['--verify'],check=True,capture_output=True)
            path=Path(d)/'data.csv'
            path.write_text('tampered')
            self.assertNotEqual(subprocess.run(cmd+['--verify'],capture_output=True).returncode,0)

class PhysicsTests(unittest.TestCase):
    def test_constant_flow_analytic_solution(self):
        values=p.simulate(2,3,[10]*100,.1,initial=0)
        self.assertAlmostEqual(values[-1],20*(1-math.exp(-10/6)),places=10)
    def test_zero_flow_decay(self):
        values=p.simulate(1,1,[0]*10,.1,initial=80)
        self.assertAlmostEqual(values[-1],80/math.e,places=10)
    def test_invalid_parameters(self):
        with self.assertRaises(ValueError): p.simulate(-1,1,[1],.1)
    def test_noiseless_parameter_recovery(self):
        cfg=json.loads((p.ROOT/'config.json').read_text())
        inflow=[80+40*math.sin(i*.1) for i in range(100)]
        truth=p.simulate(1.2,1.5,inflow,cfg['dt_seconds'])
        loss,r,c=p.calibrate(inflow,truth,cfg)
        self.assertEqual((r,c),(1.2,1.5))
        self.assertEqual(loss,0)
