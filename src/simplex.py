from typing import Callable

from src.primitives.point import Point

def find_maximum_3d(f: Callable, min_x: float, min_y: float, max_x: float, max_y: float, eps: float):
    x1 = min_x + (max_x - min_x) / 10
    y1 = min_y + (max_y - min_y) / 10

    v1 = Point(min_x, min_y)
    v2 = Point(x1, min_y)
    v3 = Point(min_x, y1)
    points_hash = str(v1) + str(v2) + str(v3)

    prev_coords_stack = []
    i = 0
    decrease_search_area = False
    while i < 1000:
        prev_coords_stack.append(points_hash)
        fv1 = f(v1.x, v1.y)
        fv2 = f(v2.x, v2.y)
        fv3 = f(v3.x, v3.y)

        # We need to switch operators for finding minimal value
        if fv1 <= fv2 and fv1 <= fv3:
            height_midpoint = Point.midpoint(v2, v3)
            height_vector = v1.vector_to(height_midpoint)
            height_vector.multiply(0.5 if decrease_search_area else 2)
            v1.add_vector(height_vector)

            if v1.x > max_x:
                v1.x = max_x
            if v1.y > max_y:
                v1.y = max_y
        elif fv2 <= fv1 and fv2 <= fv3:
            height_midpoint = Point.midpoint(v1, v3)
            height_vector = v2.vector_to(height_midpoint)
            height_vector.multiply(0.5 if decrease_search_area else 2)
            v2.add_vector(height_vector)

            if v2.x > max_x:
                v2.x = max_x
            if v2.y > max_y:
                v2.y = max_y
        elif fv3 <= fv1 and fv3 <= fv2:
            height_midpoint = Point.midpoint(v1, v2)
            height_vector = v3.vector_to(height_midpoint)
            height_vector.multiply(0.5 if decrease_search_area else 2)
            v3.add_vector(height_vector)

            if v3.x > max_x:
                v3.x = max_x
            if v3.y > max_y:
                v3.y = max_y

        if decrease_search_area:
            prev_coords_stack = []
            decrease_search_area = False

        points_hash = str(v1) + str(v2) + str(v3)
        if points_hash in prev_coords_stack:
            # It means that we started to walk in circles
            if v1.distance_to(v2) + v1.distance_to(v3) + v2.distance_to(v3) < eps:
                break

            decrease_search_area = True

        i += 1

    # Ideally we would like to take a point in the middle of the triangle, but who the fuck care
    return [v1.x, v1.y]