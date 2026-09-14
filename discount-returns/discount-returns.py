def discount_returns(rewards: list, gamma: float) -> list:
    """
    Returns the discounted return at every timestep.
    """
    # Write code here
    g = [0] * len(rewards)
    g[len(rewards)-1]= rewards[len(rewards)-1]
    for i in range(len(rewards)-2,-1,-1):
        g[i] = rewards[i] +gamma*g[i+1]
        
    
    return g