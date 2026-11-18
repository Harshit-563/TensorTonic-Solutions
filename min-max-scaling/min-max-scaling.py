def min_max_scaling(data: list) -> list:
    rows = len(data)
    cols = len(data[0])

    mins = [min(data[r][c] for r in range(rows)) for c in range(cols)]
    maxs = [max(data[r][c] for r in range(rows)) for c in range(cols)]

    result = []

    for r in range(rows):
        scaled_row = []
        for c in range(cols):
            if maxs[c] == mins[c]:
                scaled_row.append(0.0)
            else:
                scaled_row.append(
                    (data[r][c] - mins[c]) / (maxs[c] - mins[c])
                )
        result.append(scaled_row)

    return result