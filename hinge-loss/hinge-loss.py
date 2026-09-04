import numpy as np

def hinge_loss(y_true: list, y_score: list, margin: float = 1.0, reduction: str = "mean") -> float:
    """
    Returns the loss as a float.
    """
    # Write code here
    y_true = np.asarray(y_true,dtype=float)
    y_score=np.asarray(y_score,dtype=float)
    
    if reduction == "mean":
        a = np.mean(np.maximum(0.0, margin - (y_true * y_score)))
    else:
        a = np.sum(np.maximum(0.0, margin - (y_true * y_score))) 
    return float(a)    
    pass