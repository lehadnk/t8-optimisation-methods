from unittest import TestCase

from src.primitives.point import Point


class TestPoint(TestCase):
    def test_midpoint(self):
        point = Point.midpoint(Point(5, 3), Point(1, 5))
        self.assertEqual(point.x, 3)
        self.assertEqual(point.y, 4)

    def test_distance_to_point(self):
        point = Point(1, 4)
        distance = point.distance_to(Point(1, 6))
        self.assertAlmostEqual(distance, 2, 2)
