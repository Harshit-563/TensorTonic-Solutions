import numpy as np

def majority_classifier(y_train: list, X_test: list) -> np.ndarray:
    """
    Returns a one-dimensional NumPy array where each test sample
    is classified as the majority class from y_train.
    In case of a tie, the class that appears first in y_train is chosen.
    """
    y_train = np.asarray(y_train, dtype=int)
    X_test = np.asarray(X_test)

    # Find unique classes, their counts, and first occurrence indices
    classes, index, counts = np.unique(y_train, return_index=True, return_counts=True)

    max_count = np.max(counts)
    is_tied = (counts == max_count)

    if np.sum(is_tied) > 1:
        # Tie case: pick the class with smallest first occurrence index
        tied_classes = classes[is_tied]
        tied_indices = index[is_tied]
        majority_class = tied_classes[np.argmin(tied_indices)]
    else:
        # Clear majority
        majority_class = classes[np.argmax(counts)]

    # Assign majority class to all test samples
    return np.full(len(X_test), majority_class)
