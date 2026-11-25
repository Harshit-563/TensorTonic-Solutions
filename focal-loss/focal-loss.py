import numpy as np

def focal_loss(p: list, y: list, gamma: float = 2.0) -> float:
    """
    Returns the loss as a float.
    """
    p = np.asarray(p,dtype=float)
    y = np.asarray(y,dtype=float)
    l = np.mean(-1 * (1-p)**gamma * y *np.log(p)-p**gamma * (1-y)*np.log(1-p))
    return float(l)