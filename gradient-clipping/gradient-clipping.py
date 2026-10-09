import numpy as np

def clip_gradients(g: list, max_norm: float) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as g.
    """
    g = np.asarray(g,dtype=float)
    nor = np.linalg.norm(g)
    if(nor>max_norm):
        g= g*(max_norm/nor)
    return g    