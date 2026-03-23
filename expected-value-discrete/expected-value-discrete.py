import numpy as np

def expected_value_discrete(x, p):
    
    """
    Returns: float expected value
    """
    # Write code here
    x=np.array(x,dtype=float)
    p=np.array(p,dtype=float)
    b=np.sum(p)
    if b!=1 or len(x)!=len(p):
        raise ValueError("p!=1 || length of x and p mismatch ")   
    e=x*p
    a=np.sum(e,dtype=float)
    return a    
    pass
