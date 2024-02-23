import math
from typing import Callable

def find_maximum(f: Callable, min_x: float, max_x: float, eps: float):
    min = min_x
    max = max_x

    x1 = min + ((3 - math.sqrt(5)) / 2) * (max - min)
    x2 = min + ((math.sqrt(5) - 1) / 2) * (max - min)

    fx1 = f(x1)
    fx2 = f(x2)

    while True:
        print(min, max, x1, x2)

        if x2 - x1 < 2 * eps:
            print(x2, x1, 2 * eps, x2 - x1)
            break

        # We need to switch this operator for min function
        if fx1 > fx2:
            max = x2
            new_x1 = min + (x2 - x1)
            x2 = x1
            x1 = new_x1
            fx2 = fx1
            fx1 = f(x1)
        else:
            min = x1
            new_x2 = max - (x2 - x1)
            x1 = x2
            x2 = new_x2
            fx1 = fx2
            fx2 = f(x2)

    return x1 + ((x2 - x1) / 2)

