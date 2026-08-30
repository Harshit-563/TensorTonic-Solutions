import numpy as np

def auc(fpr: list, tpr: list) -> float:
    """
    Returns the area as a float.
    """
    # Write code here
    
    a =  np.diff(fpr)
    b =  0.5 * (np.array(tpr[:-1]) + np.array(tpr[1:]))
    c = a * b
    return float(np.sum(c))
    pass