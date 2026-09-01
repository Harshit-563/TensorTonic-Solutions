import numpy as np

def minmax_scale(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns a floating-point NumPy array matching the shape of X.
    """
    X = np.asarray(X, dtype=float)

    a = np.min(X, axis=axis, keepdims=True)
    b = np.max(X, axis=axis, keepdims=True)

    return (X - a) / (b - a + eps)