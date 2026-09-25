import numpy as np

def matrix_inverse(A: list) -> np.ndarray | None:
    """
    Returns the inverse as a NumPy array, or None.
    """
    A = np.asarray(A, dtype=float)
    b = np.concatenate((A, np.eye(A.shape[0])), axis=1)
    column = A.shape[1]
    for i in range(column):
        col = i + np.argmax(np.abs(b[i:, i]))
        if b[col, i] == 0:
            return None
        b[[i, col]] = b[[col, i]]
        b[i] = b[i] / b[i, i]
        for j in range(column):
            if j != i:
                b[j] = b[j] - b[j, i] * b[i]
    return b[:, column:]
