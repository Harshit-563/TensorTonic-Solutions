import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    # Write code here
    a = 0.0
    a = np.sqrt(np.sum((np.array(x)-np.array(y))**2))
    return a
    pass