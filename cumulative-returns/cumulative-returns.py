def cumulative_returns(returns: list) -> list:
    """
    Returns the compounded cumulative return after every period.
    """
    # Write code here
    wt = 1.0
    index = []
    for i in range(len(returns)):
        wt = (wt * (1+returns[i]))
        index.append(wt-1)
        
    return index
    