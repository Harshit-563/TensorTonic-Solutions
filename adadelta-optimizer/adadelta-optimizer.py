import numpy as np

def adadelta_step(w: list, grad: list, E_grad_sq: list, E_update_sq: list, rho: float = 0.9, eps: float = 1e-6) -> dict:
    """
    Returns a dictionary with new_w, new_E_grad_sq, and new_E_update_sq.
    """
    w = np.asarray(w,dtype='float')
    grad = np.asarray(grad,dtype='float')
    E_grad_sq = np.asarray(E_grad_sq,dtype='float')
    E_update_sq = np.asarray(E_update_sq,dtype='float')
    new_E_grad_sq = rho * E_grad_sq + (1-rho)*grad**2
    del_w = -1 * ((E_update_sq+eps)**0.5/(new_E_grad_sq+eps)**0.5)*grad
    new_E_update_sq=rho*E_update_sq+(1-rho)*(del_w*del_w)
    new_w = w + del_w
    
    return {"new_w": new_w, "new_E_grad_sq": new_E_grad_sq, "new_E_update_sq": new_E_update_sq}
    
    
    
    
    