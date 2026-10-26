def exponential_moving_average(values: list, alpha: float) -> list:
    """
    Returns the exponential moving average at every position.
    """
    # Write code here
    ema = [0 for _ in range(len(values))]
    ema[0] = values[0]
    for i in range(1,len(values)):
        ema[i] = alpha * values[i] + (1-alpha) * ema[i-1]
    return ema    