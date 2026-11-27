import numpy as np

def streaming_minmax(D: int, batches: list, eps: float = 1e-8) -> dict:
    batches = [np.asarray(batch, dtype=float) for batch in batches]

    running_min = batches[0].min(axis=0)
    running_max = batches[0].max(axis=0)

    normalized_batches = []

    for batch in batches:
        running_min = np.minimum(running_min, batch.min(axis=0))
        running_max = np.maximum(running_max, batch.max(axis=0))

        denom = np.maximum(running_max - running_min, eps)
        normalized_batches.append((batch - running_min) / denom)

    return {
        "normalized_batches": normalized_batches,
        "min": running_min,
        "max": running_max,
    }