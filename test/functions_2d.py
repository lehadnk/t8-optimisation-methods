import math

def f1(x: float) -> float:
    """
    [0..4] -> min 4, max pi/2
    :param x:
    :return:
    """
    return 2 * math.sin(x) + 3

def f2(x: float) -> float:
    """
    [0..4] -> min 4, max 0.368
    :param x:
    :return:
    """
    return 10 * x ** -x

def f3(x: float) -> float:
    """
    [0..5pi/2] -> min 6.437, max 3.426
    :param x:
    :return:
    """
    return -math.cos(x) * x