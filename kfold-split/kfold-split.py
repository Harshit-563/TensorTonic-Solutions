import numpy as np

def kfold_split(N, k, shuffle=False, seed=None):
    # Step 1: Create index array
    indices = np.arange(N)

    # Step 2: Optional shuffle
    if shuffle:
        indices = np.random.default_rng(seed).permutation(indices)

    # Step 3: Split into balanced validation folds
    folds = np.array_split(indices, k)

    # Step 4: Build train/validation pairs
    result = []

    for i in range(k):
        val_idx = folds[i]
        train_idx = np.concatenate([folds[j] for j in range(k) if j != i])

        result.append({
            "train_idx": train_idx,
            "val_idx": val_idx
        })

    return result