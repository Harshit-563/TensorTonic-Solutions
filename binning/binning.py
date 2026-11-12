def binning(values: list, num_bins: int) -> list:
    """
    Returns the equal-width bin index of every value.
    """
    w = (max(values)-min(values))/num_bins
    bin = []
    for i in range(len(values)):
        if w!=0 :
            a = (values[i]-min(values))//w
        else: a =  values[i]-min(values)
        b = num_bins - 1
        bin.append(min(a,b))
    return bin    