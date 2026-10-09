import numpy as np

def softmax(x: list) -> np.ndarray:
    """
    Returns stable softmax probabilities as a NumPy array matching the shape of x.
    """
    x = np.asarray(x,dtype=float)
    if(x.ndim==1):
        mx = np.max(x)
    else :    
        mx = np.max(x, axis=1, keepdims=True)
    x = x-mx   
    ex = np.exp(x)
    if(x.ndim!=1): a = ex / np.sum(ex,axis=1,keepdims=True)
    else : a = ex /np.sum(ex)   
    return a