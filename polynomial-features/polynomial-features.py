def polynomial_features(values: list, degree: int) -> list:
    """
    Returns powers from zero through degree for every value.
    """
    c=[]
    for i in values:
        a =[]
        b = 0
        while(b<=degree):
            a.append(i**b)
            b=b+1
        c.append(a)    
    return c    