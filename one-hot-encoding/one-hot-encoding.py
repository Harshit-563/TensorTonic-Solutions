import numpy as np

def one_hot(y: list, num_classes=None) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, K).
    """
    y = np.asarray(y,dtype=int)
    if (num_classes==None):
        k = np.max(y) + 1
    else:
        k = num_classes
    a = np.zeros((y.size, k), dtype=float)
    a[np.arange(y.size), y] = 1.0
    return a