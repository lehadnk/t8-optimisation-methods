from typing import Callable

def find_maximum(f: Callable, min: float, max: float, delta: float, eps: float):
    """
    :param f:
    :param min:
    :param max:
    :param delta: Половина длины отрезка поиска
    :param eps:
    :return:
    """
    j = 0
    a = min
    b = max

    segments = [[a, b]]

    while True:
        midpoint = segments[j][0] + ((segments[j][1] - segments[j][0]) / 2)
        x1 = midpoint - delta
        x2 = midpoint + delta

        # We only need to switch this operand to search for minimum
        if f(x1) > f(x2):
            segments.append([segments[j][0], midpoint])
            print(segments[j][0], midpoint, segments[j][1], x1, x2, "Left", f(x1), f(x2))
        else:
            segments.append([midpoint, segments[j][1]])
            print(segments[j][0], midpoint, segments[j][1], x1, x2, "Right", f(x1), f(x2))

        j += 1

        if (segments[j][1] - segments[j][0]) < 2 * eps:
            break

    print(segments)

    return segments[j][0] + ((segments[j][1] - segments[j][0]) / 2)