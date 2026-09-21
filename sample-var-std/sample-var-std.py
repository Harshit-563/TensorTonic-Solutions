import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x = np.asarray(x,dtype=float)
    mean = np.mean(x,dtype=float)
    var = 1/(len(x)-1)*np.sum((x-mean)**2)
    std = np.sqrt(var)
    return {"variance": float(var), "standard_deviation": float(std)}