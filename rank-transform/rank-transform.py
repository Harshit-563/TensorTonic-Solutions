def rank_transform(values: list) -> list:
    """
    Returns the one-based average rank of every value.
    """
    # Pair values with their original indices
    indexed = list(enumerate(values))
    # Sort by value
    indexed.sort(key=lambda x: x[1])

    ranks = [0] * len(values)
    i = 0
    while i < len(values):
        j = i
        # Group ties
        while j + 1 < len(values) and indexed[j+1][1] == indexed[i][1]:
            j += 1
        # Average rank for this group
        avg_rank = (i+1 + j+1) / 2.0
        for k in range(i, j+1):
            ranks[indexed[k][0]] = avg_rank
        i = j + 1

    return ranks
