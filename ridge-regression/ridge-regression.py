import numpy as np

def ridge_regression(X: list, y: list, lam: float) -> list:
    """
    Returns the ridge-regression weight vector.
    """
    I = np.identity(len(X[0]), dtype=float)
    X = np.asarray(X,dtype=float)
    y = np.asarray(y,dtype=float)
    a = np.linalg.inv(X.T @ X + lam * I) @ X.T @ y
    return a
    