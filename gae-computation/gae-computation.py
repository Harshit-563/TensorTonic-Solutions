def gae(rewards: list, values: list, gamma: float, lam: float) -> list:
    """
    Returns the generalized advantage estimate at every timestep.
    """
    dt = [0]*(len(rewards))
    for i in range(len(rewards)):
        dt[i] = rewards[i] + gamma*values[i+1] - values[i]
    at = [0]*(len(rewards))   
    at[len(rewards)-1]=dt[len(rewards)-1]
    for j in range(len(rewards)-2,-1,-1):
        at[j]=dt[j]+gamma*lam*at[j+1]
    return at    
        