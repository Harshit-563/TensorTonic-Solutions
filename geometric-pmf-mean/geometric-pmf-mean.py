import numpy as np

def geometric_pmf_mean(k: list, p: float) -> dict:
    """
    Returns a dictionary with pmf and mean.
    """
    # Write code here
    k=np.asarray(k,dtype=float)
    pmf = (1.0 - p) ** (k - 1) * p 
    mean = 1/p
    return {'pmf':pmf,'mean':mean}
    pass