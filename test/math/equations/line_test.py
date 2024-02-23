from unittest import TestCase

from src.math.equations.line import LineEquation


class TestLine(TestCase):
    def test_line_from_two_points(self):
        line = LineEquation.from_two_points(5, 3, 1, 5)
        self.assertAlmostEqual(line.m, -0.5, 2)
        self.assertAlmostEqual(line.b, 5.5, 2)

    def test_get_x(self):
        line = LineEquation.from_two_points(5, 3, 1, 5)
        self.assertAlmostEqual(line.get_x(3), 5, 2)

    def test_get_y(self):
        line = LineEquation.from_two_points(5, 3, 1, 5)
        self.assertAlmostEqual(line.get_y(5), 3, 2)

    def test_perpendicular_at_point(self):
        line = LineEquation.from_two_points(5, 3, 1, 5)
        perpendicular = line.perpendicular_at_point(3, 4)
        self.assertAlmostEqual(perpendicular.m, 2, 2)
        self.assertAlmostEqual(perpendicular.b, -2, 2)