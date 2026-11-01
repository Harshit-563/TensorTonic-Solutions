import numpy as np 
def linear_layer_forward(X: list, W: list, b: list) -> list:
    """
    Returns the affine transformation for every input row.
    """
    X = np.asarray(X,dtype=float)
    W = np.asarray(W,dtype=float)
    y = X@W + b
    return y.tolist()