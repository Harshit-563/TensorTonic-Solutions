def weighted_moving_average(values, weights):
    """
    Returns the weighted average of every complete window.
    """
    k = len(weights)
    w_sum = sum(weights)
    result = []
    for i in range(len(values) - k + 1):
        total = sum(weights[j] * values[i + j] for j in range(k))
        result.append(total / w_sum)
    return result
