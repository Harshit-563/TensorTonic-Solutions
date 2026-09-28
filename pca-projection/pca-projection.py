import numpy as np

def pca_projection(X: list, k: int) -> list:
    """
    Returns the centered data projected onto the top components.
    """
    # Write code here
    X = np.asarray(X,dtype=float)
    xc = X - np.mean(X,axis=0)
    cov = (xc.T @ xc) / (len(X)-1)
    eigvals, eigvecs = np.linalg.eigh(cov)
    indices = np.argsort(eigvals)[::-1]
    top = indices[:k]
    sorted_eigvecs = eigvecs[:, top]
    sorted_eigvecs = np.where(eigvals[top] < 0, -sorted_eigvecs, sorted_eigvecs)
 
    x = xc @ sorted_eigvecs
    return x