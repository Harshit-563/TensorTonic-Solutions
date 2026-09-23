import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a float.
    """
    # Write code here
    A = np.asarray(A,dtype=float)
    sum = 0.0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if(i==j):
                sum+=A[i][j]
    return sum