from complex import Complex
import unittest

class ComplexTest(unittest.TestCase):
    def testAdd(self):
        self.assertAlmostEqual(Complex(1.3,2) + Complex(1.7,2), Complex(3,4))