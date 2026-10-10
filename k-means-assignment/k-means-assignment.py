def k_means_assignment(points: list, centroids: list) -> list:
    assignments = []
    for p in points:
        best_dist = float("inf")
        best_idx = -1
        for j, c in enumerate(centroids):
            # Squared Euclidean distance in any dimension
            dist = sum((p[k] - c[k]) ** 2 for k in range(len(p)))
            if dist < best_dist:
                best_dist = dist
                best_idx = j
        assignments.append(best_idx)
    return assignments
