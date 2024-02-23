import math

def f1_5d(x: float, y: float, z: float, w: float, v: float):
    """
    In the span of [1,5] maxes somewhere nearby (5, 4, 3, 5, 2) and mins somewhere nearby (1, 1, 5, 1, 5)
    :param x:
    :param y:
    :param z:
    :param w:
    :param v:
    :return:
    """
    return x ** 2 + 3 * math.cos(y + 2) + 2 * math.sin(z - 1) + w ** 0.5 + v * math.sin(v)

def f2_5d(x: float, y: float, z: float, w: float, v: float):
    """
    In the span of [1,5] maxes somewhere nearby (5, 5, 5, 5, 5) and mins somewhere nearby (1, 1, 1, 1, 1)
    :param x:
    :param y:
    :param z:
    :param w:
    :param v:
    :return:
    """
    return x + y + z + w + v