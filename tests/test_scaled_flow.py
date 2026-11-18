import math,unittest
import pipeline as p
class ScaledFlowTests(unittest.TestCase):
 def test_intermediate_overflow_avoided(self):
  dt=.001;expected=1e308*(2*(-math.expm1(-dt)))
  actual=p.simulate(1e308,1e-308,[2],dt,initial=0)[0]
  self.assertTrue(math.isclose(actual,expected,rel_tol=1e-14))
 def test_intermediate_underflow_avoided(self):
  actual=p.simulate(1e308,1e-308,[1e-308],1e-100,initial=0)[0]
  self.assertTrue(math.isclose(actual,1e-100,rel_tol=1e-14))
 def test_signed_zero_and_nonrepresentable_products(self):
  self.assertEqual(p.finite_product(-2,3,.5),-3)
  self.assertEqual(p.finite_product(0,1e308,1e308),0)
  for xs in [(1e308,1e308),(float('nan'),1),(float('inf'),0)]:
   with self.assertRaises(ValueError):p.finite_product(*xs)
