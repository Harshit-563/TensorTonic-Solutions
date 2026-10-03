import numpy as np

def kl_divergence(p: list, q: list, eps: float = 1e-12) -> float:
    """
    Returns the divergence as a float.
    """
    # Write code here
    p=np.asarray(p,dtype=float)
    q=np.asarray(q,dtype=float)
    positive = p > 0
    p = np.delete(p, np.where(p == 0))
    a=0.0
    a+=np.sum(p*np.log(p/np.clip(q[positive], eps, None)))
    return float(a)
    
    
    