from complex import Complex
import unittest

class ComplexTest(unittest.TestCase):
    def testSub(self):
        s = Complex(1.3,2) - Complex(1.7,2)
        self.assertAlmostEqual(s, Complex(-0.4,0))

    def testAdd(self):
        s = Complex(1.3,2) + Complex(1.7,2)
        self.assertAlmostEqual(s, Complex(3,4))