import numpy as np

def compute_advantage(states: list, rewards: list, V: list, gamma: float) -> np.ndarray:
    """
    Returns the advantages as a NumPy array.
    """
    # Write code here
    g=[0] * (len(rewards))
    a=[0]*len(rewards)
    for i in range(len(rewards)-1,-1,-1):
        g[i] = rewards[i] + gamma*(g[i+1] if (i+1) < len(rewards) else 0)
        a[i] = g[i] -  V[states[i]]
    a = np.asarray(a,dtype=float)
    return np.round(a,4)
        