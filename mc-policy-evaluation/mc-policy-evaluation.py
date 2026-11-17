import numpy as np

def mc_policy_evaluation(episodes: list, gamma: float, n_states: int) -> np.ndarray:
    returns_sum = np.zeros(n_states)
    returns_count = np.zeros(n_states)

    for episode in episodes:
        T = len(episode)
        returns = [0] * T

        # Backward pass: compute G_t
        G = 0
        for t in range(T - 1, -1, -1):
            state, reward = episode[t]
            G = reward + gamma * G
            returns[t] = G

        # Forward pass: first-visit MC
        visited = set()
        for t in range(T):
            state, reward = episode[t]

            if state not in visited:
                visited.add(state)
                returns_sum[state] += returns[t]
                returns_count[state] += 1

    values = np.zeros(n_states)
    for s in range(n_states):
        if returns_count[s] > 0:
            values[s] = returns_sum[s] / returns_count[s]

    return values