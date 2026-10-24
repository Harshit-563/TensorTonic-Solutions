import numpy as np

def silhouette_score(X: list, labels: list[int]) -> float:
    """
    Returns the mean Silhouette Score as a Python float.
    """
    X = np.asarray(X, dtype=float)
    labels = np.asarray(labels)

    # Pairwise Euclidean distances
    dist = np.linalg.norm(
        X[:, None, :] - X[None, :, :],
        axis=2
    )

    n = len(labels)
    unique_labels = np.unique(labels)

    silhouettes = []

    for i in range(n):
        own_cluster = labels[i]

        # a(i): average distance to points in same cluster
        same = labels == own_cluster
        same[i] = False

        if np.sum(same) == 0:
            silhouettes.append(0.0)
            continue

        a = dist[i, same].mean()

        # b(i): minimum average distance to another cluster
        b = float("inf")

        for cluster in unique_labels:
            if cluster == own_cluster:
                continue

            other = labels == cluster
            b = min(b, dist[i, other].mean())

        silhouettes.append((b - a) / max(a, b))

    return float(np.mean(silhouettes))
