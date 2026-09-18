import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    # Write code here
    X = np.asarray(X,dtype=float)
    N = X.shape[0]
    mean = np.mean(X,axis=0)
    centered = X - mean
    covariance = centered.T @ centered / (N - 1)
    sigma = np.sqrt(np.diag(covariance))
    return  covariance/np.outer(sigma,sigma)
    