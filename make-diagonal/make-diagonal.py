import numpy as np

def make_diagonal(v: list) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, N).
    """
    # Write code here
    v = np.asarray(v,dtype=float)
    a = np.zeros((len(v),len(v)),dtype=float)
    for i in range(len(v)):
        for j in range(len(v)):
            if(i==j):
                a[i][j]=v[i]
    return a