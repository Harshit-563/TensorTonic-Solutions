import math

def poisson_pmf_cdf(lam: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    p = math.exp(-1*lam)*(lam)**k/math.factorial(k)
    cdf = 0.0
    for i in range(k+1):
        cdf +=  math.exp(-1*lam)*(lam)**i/math.factorial(i)
    return  { "pmf": p, "cdf": cdf}  
    