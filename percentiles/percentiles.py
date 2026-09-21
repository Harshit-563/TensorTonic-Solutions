import numpy as np

def percentiles(x: list, q: list) -> np.ndarray:
    """
    Returns a NumPy array of percentiles.
    """
    # Write code here
    x=np.asarray(x,dtype=float)
    q=np.asarray(q,dtype=float)
    x=np.sort(x)
    r = q/100*(len(x)-1)
    l = np.floor(r).astype(int)
    u = np.ceil(r).astype(int)
    w =r-l
    p = (1-w)*x[l] + w*x[u]
    return p