import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    X = np.asarray(X,dtype='float')
    X = X-np.mean(X,axis=0)
    N = X.shape[0]
    return (X.T @ X) / (N-1)