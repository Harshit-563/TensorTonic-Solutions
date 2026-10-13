import math

def label_smoothing_loss(predictions: list, target: int, epsilon: float) -> float:
    """
    Returns cross-entropy loss for the smoothed target distribution.
    """
    a =[]
    for i in range(len(predictions)):
        if(i!=target):
            a.append(epsilon/len(predictions))
        else:
            a.append((1-epsilon)+epsilon/len(predictions))
            
    l = 0.0
    for i in range(len(predictions)):
        l += -1*a[i]*math.log(predictions[i])
    return l;