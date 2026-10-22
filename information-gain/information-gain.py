import numpy as np

def information_gain(y: list, split_mask: list) -> float:
    """
    Returns the information gain as a float.
    """
    y = np.asarray(y)

    # Parent entropy
    _, counts = np.unique(y, return_counts=True)
    p = counts / len(y)
    h = -np.sum(p * np.log2(p))

    split_mask = np.asarray(split_mask, dtype=bool)

    # Left and right splits
    yl = y[split_mask]
    yr = y[~split_mask]

    # Left entropy
    _, counts_l = np.unique(yl, return_counts=True)
    p_l = counts_l / len(yl)
    h_l = -np.sum(p_l * np.log2(p_l))

    # Right entropy
    _, counts_r = np.unique(yr, return_counts=True)
    p_r = counts_r / len(yr)
    h_r = -np.sum(p_r * np.log2(p_r))

    # Information Gain
    ig = h - (len(yl) / len(y)) * h_l - (len(yr) / len(y)) * h_r

    return float(ig)