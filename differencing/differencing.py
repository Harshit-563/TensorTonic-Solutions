def differencing(series: list, order: int) -> list:
    """
    Returns the series after the requested differencing order.
    """
    while order>0:
        for i in range(len(series)-1):
            series[i] = series[i+1] - series[i]
        series.pop()
        order = order - 1    
    return series        
   