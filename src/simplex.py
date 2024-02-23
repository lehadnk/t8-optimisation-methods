import math
from typing import Callable

def truncate(n, decimals=0):
    multiplier = 10**decimals
    return int(n * multiplier) / multiplier

def simplex_hash(vertices):
    result = ""
    for v in vertices:
        for c in v:
            result += str(truncate(c, 10))

    return result

def find_maximum_md(f: Callable, args_amount: int, start: float, end: float, eps: float):
    adjusted_coordinate = start + (end - start) / 10

    """
    Now we're creating a set of args_amount + 1 n-th dimensional points (simplex vertices) with every
    point having a unique coordinate:
    (min, min, min, min, min)
    (adjusted_coord, min, min, min, min)
    (min, adjusted_coord, min, min, min)
    (min, min, adjusted_coord, min, min)
    ...
    (min, min, min, min, min, adjusted_coord)
    """
    simplex_vertices = [[start for j in range(0, args_amount)]]
    for i in range(0, args_amount):
        coords = [start for j in range(0, args_amount)]
        coords[i] = adjusted_coordinate
        simplex_vertices.append(coords)

    """
    We're gonna use hashed values to determinate if we start walking in circles. Generally, making circle means
    that we're somewhere close to extremum point, and we have to decrease simplex size to increase algorithm precision
    """
    prev_coord_hashes_stack = []
    hash = simplex_hash(simplex_vertices)

    iterations = 0
    min_value_index = 0
    decrease_search_area = False
    while iterations < 1000:
        prev_coord_hashes_stack.append(hash)

        values = [f(*v) for v in simplex_vertices]
        min_value_index = values.index(min(values))

        """
        Now we have to define a vector connecting the weakest vertex with a center of opposite side of the simplex
        (which will be the median) and then multiply it by 2 if we want to move point one step forward, or by 0.5
        if we want to increase the algorithm precision 
        """
        median_midpoint = []
        for i in range(0, args_amount):
            # Midpoint is the sum of point coordinates for this particular dimension divided by the amount of points
            midpoint_coordinate = (sum([c[i] for c in simplex_vertices]) - simplex_vertices[min_value_index][i]) / args_amount
            median_midpoint.append(midpoint_coordinate)

        vertex_adjustment_vector = [median_midpoint[i] - simplex_vertices[min_value_index][i] for i in range(0, args_amount)]
        vertex_adjustment_vector = [x * 0.5 if decrease_search_area else x * 2 for x in vertex_adjustment_vector]

        simplex_vertices[min_value_index] = [simplex_vertices[min_value_index][i] + vertex_adjustment_vector[i] for i in range(0, args_amount)]

        # This way we don't let algorithm go outside the search zone
        for i in range(0, args_amount):
            if simplex_vertices[min_value_index][i] > end:
                simplex_vertices[min_value_index][i] = end
            if simplex_vertices[min_value_index][i] < start:
                simplex_vertices[min_value_index][i] = start

        if decrease_search_area:
            decrease_search_area = False

            # New edge size is generally the distance from the moved vertex to any other vertex
            edge_size = math.sqrt(sum([(simplex_vertices[min_value_index][i] - simplex_vertices[min_value_index - 1][i]) ** 2 for i in range(0, args_amount)]))
            if edge_size < eps:
                break

        hash = simplex_hash(simplex_vertices)
        if hash in prev_coord_hashes_stack:
            decrease_search_area = True
            prev_coord_hashes_stack = []

        iterations += 1

    """
    Ideally we would like to give it another round and return the middle point of all vertices, but doesn't worth the
    computational power
    """
    return simplex_vertices[min_value_index]