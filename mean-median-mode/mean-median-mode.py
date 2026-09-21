from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    mean = np.mean(x);
    median = np.median(x)
    count = Counter(x)
    mode = count.most_common(1)[0]
    return {"mean": float(mean), "median": float(median), "mode": float(mode[0])}
    pass