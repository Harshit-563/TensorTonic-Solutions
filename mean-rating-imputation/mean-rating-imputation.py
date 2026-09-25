def mean_rating_imputation(ratings_matrix: list, mode: str) -> list:
    """
    Returns a copy with missing ratings replaced by user or item means.
    Missing ratings are assumed to be 0.
    """
    import copy
    matrix = copy.deepcopy(ratings_matrix)
    rows, cols = len(matrix), len(matrix[0])

    if mode == 'user':
        for i in range(rows):
            # compute mean of non-zero ratings for user i
            non_zero = [matrix[i][j] for j in range(cols) if matrix[i][j] != 0]
            mean_val = sum(non_zero) / len(non_zero) if non_zero else 0
            for j in range(cols):
                if matrix[i][j] == 0:
                    matrix[i][j] = mean_val

    elif mode == 'item':
        for j in range(cols):
            # compute mean of non-zero ratings for item j
            non_zero = [matrix[i][j] for i in range(rows) if matrix[i][j] != 0]
            mean_val = sum(non_zero) / len(non_zero) if non_zero else 0
            for i in range(rows):
                if matrix[i][j] == 0:
                    matrix[i][j] = mean_val

    else:
        raise ValueError("mode must be 'user' or 'item'")

    return matrix
