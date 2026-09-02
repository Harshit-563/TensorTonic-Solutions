import numpy as np

def huber_loss(y_true: list, y_pred: list, delta: float = 1.0) -> float:
    """
    Returns the loss as a float.
    """
    # Write code here
    loss = 0.0
    y_pred = np.asarray(y_pred,dtype=float)
    y_true = np.asarray(y_true,dtype=float)
    for i,j in zip(y_pred,y_true):
        a = abs(i - j)
        if(a<=delta):
            loss+=0.5*(a**2)
        else:
            loss+=(delta*(abs(a)-(0.5*delta)))

    return float(loss)/len(y_pred)
    pass