import numpy as np

def time_based_split(timestamps: list, train_end: int, gap: int, val_end: int) -> dict:
    """
    Returns a dictionary with train_idx and val_idx as sorted integer NumPy arrays.

    Parameters:
        timestamps: List of timestamps (assumed sortable).
        train_end: End timestamp for the training period (inclusive).
        gap: Number of time units to exclude between train and validation.
        val_end: End timestamp for the validation period (inclusive).

    Returns:
        {
            "train_idx": np.ndarray,
            "val_idx": np.ndarray
        }
    """
    timestamps = np.asarray(timestamps)

    train_idx = np.where(timestamps < train_end)[0]
    val_idx = np.where(
        (timestamps >= train_end + gap) &
        (timestamps < val_end)
    )[0]

    return {
        "train_idx": train_idx.astype(int),
        "val_idx": val_idx.astype(int)
    }