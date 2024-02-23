class LineEquation:
    def __init__(self, m: float, b: float):
        """
        Creates a line from slope and adjustment modifiers (m and b in the default line equation: y = mx + b)
        :param m: Slope modifier
        :param b: Adjustment
        :return:
        """
        self.m = m
        self.b = b

    @staticmethod
    def from_two_points(p1x: float, p1y: float, p2x: float, p2y: float):
        """
        Creates a line crossing two points
        Slope is y2-y2 / x2 - x1
        Adjustment modifier may be found by replacing x and y with point coordinates and solving the line equation: y = mx + b <-> b = -mx + y
        :param m: Slope modifier
        :param b: Adjustment
        :return:
        """
        m = (p2y - p1y) / (p2x - p1x)
        return LineEquation(
            m,
            -m * p1x + p1y
        )

    def perpendicular_with_adjustment(self, b: float):
        return LineEquation(1 / self.m, b)

    def perpendicular_at_point(self, x: float, y: float):
        m = -1 / self.m
        b = -m * x + y
        return LineEquation(m, b)

    def get_x(self, y: float):
        return (self.b - y) / -self.m

    def get_y(self, x: float):
        return x * self.m + self.b