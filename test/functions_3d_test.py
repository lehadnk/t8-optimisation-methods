import unittest
from functions_3d import f3

class TestFunctions3dMethods(unittest.TestCase):
    def test_f3(self):
        self.assertAlmostEqual(f3(0, 0), 1 / 3, 2)