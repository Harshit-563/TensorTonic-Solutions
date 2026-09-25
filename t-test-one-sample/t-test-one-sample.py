import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    # Write code here
    x = np.asarray(x,dtype=float)
    s = np.sqrt(np.sum((x-np.mean(x))**2)/(x.size-1))
    t = (np.mean(x)-mu0)/(s/np.sqrt(x.size))
    return float(t)
    