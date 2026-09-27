import numpy as np

def bootstrap_mean(x: list, n_bootstrap: int = 1000, ci: float = 0.95, seed: int = 0) -> dict:
    """
    Returns a dictionary with bootstrap_mean, lower, and upper.
    """
    rng = np.random.default_rng(seed)
    x = np.asarray(x, dtype=float)
    
    # Generate bootstrap samples
    indices = rng.integers(0, x.size, size=(n_bootstrap, x.size))
    samples = x[indices].mean(axis=1)
    
    # Compute mean and confidence interval
    boot_mean = samples.mean()
    lower = np.percentile(samples, (1 - ci) / 2 * 100)
    upper = np.percentile(samples, (1 + ci) / 2 * 100)
    
    return {'bootstrap_mean': boot_mean, 'lower': lower, 'upper': upper}
