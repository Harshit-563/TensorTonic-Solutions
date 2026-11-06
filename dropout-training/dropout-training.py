import numpy as np

def dropout(
    x: list,
    p: float = 0.5,
    rng: np.random.Generator = None,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Returns (output, dropout_pattern) as NumPy arrays matching the shape of x.
    """
    x = np.asarray(x, dtype=float)

    keep_prob = 1.0 - p

    if rng is None:
        r = np.random.random(x.shape)
    else:
        r = rng.random(x.shape)

    dropout_pattern = (r < keep_prob).astype(float) / keep_prob
    output = x * dropout_pattern

    return output, dropout_pattern