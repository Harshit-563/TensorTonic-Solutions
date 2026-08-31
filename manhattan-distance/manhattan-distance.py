import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    # Write code here
    a = 0.0
    for i, j in zip(x, y):
        a += abs(i - j)
    return a
    pass