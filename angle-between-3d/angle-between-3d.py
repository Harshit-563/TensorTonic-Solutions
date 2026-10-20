import numpy as np

def angle_between_3d(v: list, w: list) -> float:
    """
    Returns the angle as a float.
    """
    v = np.asarray(v,dtype=float)
    w = np.asarray(w,dtype=float)
    a = np.dot(v,w)/np.sqrt(np.sum(np.square(v))*(np.sum(np.square(w))))
    c = np.clip(a,-1.0,1.0)
    b = np.arccos(c)
    return b