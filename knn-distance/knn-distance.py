import numpy as np

def knn_distance(X_train: list, X_test: list, k: int) -> np.ndarray:
    """
    Returns a NumPy array with shape (n_test, k),
    containing indices of the k nearest neighbors in X_train for each test sample.
    If k > len(X_train), pads with -1.
    """
    # Convert to arrays
    X_train = np.asarray(X_train, dtype=float)
    X_test = np.asarray(X_test, dtype=float)

    # Reshape scalars/1D datasets to (-1,1)
    if X_train.ndim == 1:
        X_train = X_train.reshape(-1, 1)
    if X_test.ndim == 1:
        X_test = X_test.reshape(-1, 1)

    # Compute squared distances: shape (n_test, n_train)
    dists = np.sum((X_test[:, None, :] - X_train[None, :, :]) ** 2, axis=2)

    # Sort indices by distance
    sorted_indices = np.argsort(dists, axis=1)

    # Take available neighbors
    n_train = X_train.shape[0]
    neighbors = sorted_indices[:, :min(k, n_train)]

    # Pad with -1 if k > n_train
    if k > n_train:
        pad = -1 * np.ones((neighbors.shape[0], k - n_train), dtype=int)
        neighbors = np.concatenate([neighbors, pad], axis=1)

    return neighbors
