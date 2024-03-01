import unittest
from functions_3d import f1, f2, f3
from functions_5d import f1_5d, f2_5d
from src.simplex import find_maximum_md
import math

class TestSimplexMethods(unittest.TestCase):
    def test_f1(self):
        max_x, max_y = find_maximum_md(f1, 2, 0, 3, 0.01)
        self.assertAlmostEqual(max_x, math.pi / 2, 2)
        self.assertAlmostEqual(max_y, math.pi / 2, 2)

    def test_f2(self):
        max_x, max_y = find_maximum_md(f2, 2, 0.01, 4, 0.01)
        self.assertAlmostEqual(max_x, 4, 2)
        self.assertAlmostEqual(max_y, 4, 2)

    def test_f3(self):
        max_x, max_y = find_maximum_md(f3, 2, 0, 1.8, 0.01)
        self.assertAlmostEqual(max_x, 1.8, 2)
        self.assertAlmostEqual(max_y, 0.239, 2)

    def test_f1_5d(self):
        max_x, max_y, max_z, max_w, max_v = find_maximum_md(f1_5d, 5, 1, 5, 0.001)
        self.assertAlmostEqual(max_x, 5, 2)
        self.assertAlmostEqual(max_y, 4.28, 2)
        self.assertAlmostEqual(max_z, 2.57, 2)
        self.assertAlmostEqual(max_w, 5, 2)
        self.assertAlmostEqual(max_v, 2, 1)

    def test_f2_5d(self):
        max_x, max_y, max_z, max_w, max_v = find_maximum_md(f2_5d, 5, 1, 5, 0.01)
        self.assertAlmostEqual(max_x, 5, 2)
        self.assertAlmostEqual(max_y, 5, 2)
        self.assertAlmostEqual(max_z, 5, 2)
        self.assertAlmostEqual(max_w, 5, 2)
        self.assertAlmostEqual(max_v, 5, 2)