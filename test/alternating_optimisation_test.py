import unittest
from functions_3d import f1, f2, f3
from src.alternating_optimisation import find_maximum_3d
import math

class TestAlternatingOptimisationMethods(unittest.TestCase):
    def test_f1(self):
        maxX, maxY = find_maximum_3d(f1, 0, 0, 3, 3, 0.1, 0.001, 2)
        self.assertAlmostEqual(maxX, math.pi / 2, 2)
        self.assertAlmostEqual(maxY, math.pi / 2, 2)

    def test_f2(self):
        maxX, maxY = find_maximum_3d(f2, 0.01, 0.01, 4, 4, 0.1, 0.001, 2)
        self.assertAlmostEqual(maxX, 4, 2)
        self.assertAlmostEqual(maxY, 4, 2)

    def test_f3(self):
        maxX, maxY = find_maximum_3d(f3, 0, 0, 1.8, 2, 0.1, 0.001, 1)
        self.assertAlmostEqual(maxX, 1.8, 2)
        self.assertAlmostEqual(maxY, 0.239, 2)