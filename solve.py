from src.alternating_optimisation import find_maximum_3d

def func(x: float, y: float):
    if (1.5 * 2 + 2 * y) > 150:
        return 0

    if (1.25 * x + y) > 100:
        return 0

    if x < 20:
        return 0

    if y < 30:
        return 0

    return 100 * x + 80 * y

varX, varY = find_maximum_3d(func, 30, 30, 56, 36, 0.001, 0.01, 5)

print("X: ", varX, "Y: ", varY, "Z: ", func(varX, varY))