import numpy as np

def cross_entropy_loss(y_true: list[int], y_pred: list[list[float]]) -> float:
    """
    Returns the mean multiclass cross-entropy loss as a Python float.
    """
    y_pred = np.asarray(y_pred,dtype='float')
    y_true = np.asarray(y_true,dtype='int')
    row_indices=np.arange(len(y_true))
    a=-1*np.mean(np.log(y_pred[row_indices, y_true]))
    return a