import numpy as np

def gini_impurity(y_left: list, y_right: list) -> float:
    y_left, y_right = np.asarray(y_left), np.asarray(y_right)
    n_left, n_right = len(y_left), len(y_right)
    total = n_left + n_right
    if total == 0:   # avoid division by zero
        return 0.0

    def gini(y):
        if y.size == 0: return 0.0
        _, counts = np.unique(y, return_counts=True)
        p = counts / counts.sum()
        return 1.0 - np.sum(p*p)

    return (n_left/total)*gini(y_left) + (n_right/total)*gini(y_right)
