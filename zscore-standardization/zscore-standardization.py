import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns population Z-scores as a NumPy array matching the shape of X.
    """
    # Write code here
    X = np.asarray(X, dtype=float)

    a = np.mean(X, axis=axis, keepdims=True)
    b = np.std(X, axis=axis, keepdims=True)
    c =  np.where(b > eps, b, 1.0)

    return (X - a) / (c)
    pass