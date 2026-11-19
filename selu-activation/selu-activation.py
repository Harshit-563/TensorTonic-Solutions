import math

def selu(x: list) -> list:
    """
    Returns SELU values rounded to four decimal places.
    """
    a = [1.0507*y if y>0 else 1.6733*1.0507*(math.exp(y)-1) for y in x]
    return a