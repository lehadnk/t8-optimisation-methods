import math

from src.primitives.vector import Vector


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @staticmethod
    def midpoint(p1, p2):
        return Point(
            (p1.x + p2.x) / 2,
            (p1.y + p2.y) / 2
        )

    def distance_to(self, p):
        return math.sqrt(math.fabs(self.x - p.x) ** 2 + math.fabs(self.y - p.y) ** 2)

    def vector_to(self, p):
        return Vector(
            p.x - self.x,
            p.y - self.y
        )

    def add_vector(self, v: Vector):
        self.x += v.x
        self.y += v.y

    def __str__(self):
        return "(" + str(self.x) + " " + str(self.y) + ")"