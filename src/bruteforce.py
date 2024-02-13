from typing import Callable

def find_maximum(f: Callable, min: float, max: float, eps: float):
    max_result = None
    i_giving_max_result = min

    i = min
    while i < max:
        r = f(i)
        if max_result is None or r > max_result:
            max_result = r
            i_giving_max_result = i
        i += eps

    return i_giving_max_result