
def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    while steps>0:
        f=a*x0**2+b*x0+c
        f1=2*a*x0+b
        x0=x0-(lr*f1)
        steps=steps-1
        
    return x0
    pass