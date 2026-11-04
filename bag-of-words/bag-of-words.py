import numpy as np

def bag_of_words_vector(tokens: list, vocab: list) -> np.ndarray:
    """
    Returns a NumPy array with length len(vocab).
    Each element is the count of the corresponding vocabulary word in tokens.
    """
    token_counts = {}
    for token in tokens:
        token_counts[token] = token_counts.get(token, 0) + 1

    return np.array([token_counts.get(word, 0) for word in vocab])