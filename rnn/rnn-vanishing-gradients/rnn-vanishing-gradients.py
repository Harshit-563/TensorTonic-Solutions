import numpy as np

def compute_gradient_norm_decay(T: int, W_hh: np.ndarray) -> np.ndarray:
    """
    Returns T float64 spectral-norm powers.
    """
    a = np.linalg.norm(W_hh, ord=2)
    b = np.arange(T)
    gk = a ** b
    return gk    
        
        