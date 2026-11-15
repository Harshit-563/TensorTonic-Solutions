import numpy as np

def batch_norm_forward(x: list, gamma: list, beta: list, eps: float = 1e-5) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    x=np.asarray(x,dtype=float)
    gamma=np.asarray(gamma,dtype=float)
    beta=np.asarray(beta,dtype=float) 
    axes = (0,) if x.ndim == 2 else (0, 2, 3)
    miu = np.mean(x,axis=axes,keepdims=True )
    var=np.var(x,axis=axes,keepdims=True )
    a=(x-miu)/np.sqrt(var+eps)
    C = x.shape[1]
    b = gamma.reshape(1, C, 1, 1)
    c = beta.reshape(1, C, 1, 1)
    if(x.ndim == 4):
        return b * a + c
    else:
        return gamma * a + beta