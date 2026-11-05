import numpy as np

def stratified_split(X: list, y: list, test_size: float = 0.2, seed: int = 42) -> dict:
    """
    Returns a dictionary with X_train, X_test, y_train, and y_test.
    """
    # Step 1: Convert to NumPy arrays
    X = np.asarray(X)
    y = np.asarray(y)

    # Step 2: Create one RNG for all classes
    rng = np.random.default_rng(seed)

    train_idx = []
    test_idx = []

    # Step 3: Process each class
    for cls in np.unique(y):
        class_idx = np.flatnonzero(y == cls)
        n_class = len(class_idx)

        # Number of test samples for this class
        n_test = int(round(n_class * test_size))

        # Ensure at least one sample remains in train
        if n_class > 1:
            n_test = min(n_test, n_class - 1)

        # Step 4: Shuffle class indices
        shuffled_idx = rng.permutation(class_idx)

        # First n_test samples go to test
        test_idx.extend(shuffled_idx[:n_test])

        # Remaining samples go to train
        train_idx.extend(shuffled_idx[n_test:])

    # Sort to preserve original order in outputs
    train_idx = np.sort(train_idx)
    test_idx = np.sort(test_idx)

    return {
        "X_train": X[train_idx],
        "X_test": X[test_idx],
        "y_train": y[train_idx],
        "y_test": y[test_idx]
    }
