import unittest
from functions_2d import f1, f2, f3
from src.dichotomy import find_maximum
import math

class TestDichotomyMethods(unittest.TestCase):
    def test_f1(self):
        max = find_maximum(f1, 0, 4, 0.1, 0.01)
        self.assertAlmostEqual(max, math.pi / 2, 2)

    def test_f2(self):
        max = find_maximum(f2, 0, 4, 0.1, 0.01)
        self.assertAlmostEqual(max, 0.368, 2)

    def test_f3(self):
        max = find_maximum(f3, 0, 5 * math.pi / 2, 0.1, 0.01)
        self.assertAlmostEqual(max, 3.426, 2)