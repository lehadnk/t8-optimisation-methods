from typing import Callable
from src.dichotomy import find_maximum

def find_maximum_3d(f: Callable, min_x: float, min_y: float, max_x: float, max_y: float, delta: float, eps: float, iterations: int):
    var_x = min_x
    var_y = min_y

    x_direction = True

    i = 0
    while i < iterations * 2:
        if x_direction:
            print("Testing X", var_x, min_x, max_x)
            var_x = find_maximum(lambda x: f(x, var_y), min_x, max_x, delta, eps)
            # var_x = find_maximum(lambda x: f(x, var_y), min_x, max_x, eps)
            print("New X:", var_x)
        else:
            print("Testing Y", var_y, min_y, max_y)
            var_y = find_maximum(lambda y: f(var_x, y), min_y, max_y, delta, eps)
            # var_y = find_maximum(lambda y: f(var_x, y), min_y, max_y, eps)
            print("New Y:", var_y)

        x_direction = not x_direction
        i += 1

    return var_x, var_y