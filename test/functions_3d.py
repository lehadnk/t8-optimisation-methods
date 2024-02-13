import math

def f1(x: float, y: float) -> float:
    """
    [0..3][0..3] -> max pi/2, pi/2
    :param x:
    :return:
    """
    return math.sin(x) + 2 * math.sin(y)

def f2(x: float, y: float) -> float:
    """
    [0..4][0..4] -> max 4, 4
    :param x:
    :return:
    """
    return (x * y) / 4

def f3(x: float, y: float) -> float:
    """
    [0..2][0..2] -> max 2, 0.23
    :param x:
    :return:
    """
    return (math.cos(x * y) / 3) + x / 2 + y / 4