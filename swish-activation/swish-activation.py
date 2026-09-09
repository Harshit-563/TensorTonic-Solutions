import numpy as np

def swish(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    x=np.asarray(x, dtype=float)
    t=np.exp(-np.logaddexp(0.0, -x)) 
    return np.asarray(x*t)
    pass