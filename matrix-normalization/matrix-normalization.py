import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    # Write code here
    matrix = np.asarray(matrix,dtype=float)
    
    if(norm_type=='l1'):
        norm = np.sum(matrix, axis=axis, keepdims=True)
        div = np.where(norm == 0, 1.0, norm)
        matrix = matrix/div
    elif(norm_type=='l2'):
        norm = np.sqrt(np.sum(np.square(matrix),axis=axis,keepdims=True))
        div = np.where(norm == 0, 1.0, norm)
        matrix = matrix/div  
    else:
        norm = np.max(matrix,axis=axis,keepdims=True)
        div = np.where(norm == 0, 1.0, norm)
        matrix = matrix/div  
    return matrix                   
        
        
    