def k_means_centroid_update(points: list, assignments: list, k: int) -> list:
    """
    Returns one updated centroid for each cluster.
    Each centroid is the mean of points assigned to that cluster.
    If a cluster has no points, return a zero vector of the same dimension.
    """
    if not points:
        return []

    dim = len(points[0])  # number of features per point
    centroids = [[0.0] * dim for _ in range(k)]
    counts = [0] * k

    # Accumulate sums for each cluster
    for p, cluster in zip(points, assignments):
        counts[cluster] += 1
        for d in range(dim):
            centroids[cluster][d] += p[d]

    # Divide sums by counts to get means
    for j in range(k):
        if counts[j] > 0:
            centroids[j] = [val / counts[j] for val in centroids[j]]
        else:
            centroids[j] = [0.0] * dim  # handle empty cluster

    return centroids
