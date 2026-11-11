import numpy as np

def initialize_mcts_edges(policy_logits: np.ndarray,
                          legal_mask: np.ndarray) -> dict:

    P = np.zeros_like(policy_logits, dtype=np.float64)

    legal = legal_mask.astype(bool)

    logits = policy_logits[legal]
    exp_logits = np.exp(logits - np.max(logits))
    P[legal] = exp_logits / exp_logits.sum()

    return {
        "N": np.zeros_like(policy_logits, dtype=np.int64),
        "W": np.zeros_like(policy_logits, dtype=np.float64),
        "Q": np.zeros_like(policy_logits, dtype=np.float64),
        "P": P,
    }