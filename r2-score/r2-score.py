import numpy as np

def r2_score(y_true: list, y_pred: list) -> float:
    """
    Returns the coefficient of determination as a Python float.
    """
    # Write code here
    y_pred = np.asarray(y_pred,dtype=float)
    y_true = np.asarray(y_true,dtype=float)
    a = np.sum((y_true - y_pred) ** 2)
    b = np.sum((y_true-np.mean(y_true))**2)
    
    if(b==0):
        if(y_true.all()==y_pred.all()):
            return 1.0
        else:
            return 0.0
    return float(1-(a/b))
    pass