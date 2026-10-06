import math

def gaussian_kernel(size: int, sigma: float) -> list:
    """
    Returns a square two-dimensional list.
    """
    # Write code here
    cen = size//2
    a = []
    tot = 0.0
    for i in range(size):
        b=[]
        for j in range(size):
            x = i - cen
            y = j - cen
            c = math.exp(-1*((x**2 + y**2)/(2*(sigma**2))))
            tot+=c
            b.append(c)
        a.append(b)    
    for i in range(size):
        for j in range(size):
            a[i][j]=a[i][j]/tot
    return a        