class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def multiply(self, scalar: float):
        self.x = self.x * scalar
        self.y = self.y * scalar

    def __str__(self):
        return "[" + str(self.x) + " " + str(self.y) + "]"