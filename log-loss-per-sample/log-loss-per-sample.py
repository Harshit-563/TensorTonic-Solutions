import math
import numpy as np

def log_loss(y_true: list, y_pred: list, eps: float = 1e-15) -> list:
    """
    Returns a list of loss values.
    """
    # Write code here
    y_pred=np.asarray(y_pred,dtype=float)
    y_true=np.asarray(y_true,dtype=float)
    loss = []
    for i in range(len(y_true)):
        p = max(eps, min(1 - eps, y_pred[i]))
        y = y_true[i]
        loss.append(-(y * math.log(p) + (1 - y) * math.log(1 - p)))    
    return loss    