import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    y = np.array(y)
    
    # Get counts of unique values
    _, counts = np.unique(y, return_counts=True)
    
    # Convert counts to probabilities
    p = counts / len(y)
    
    # Avoid log(0) by masking
    p = p[p > 0]
    
    # Compute entropy
    h = -np.sum(p * np.log2(p))
    
    return h
    pass