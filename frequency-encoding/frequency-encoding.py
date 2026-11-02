def frequency_encoding(values: list) -> list:
    """
    Returns the relative frequency of every input value.
    """
    count = {}

    for x in values:
        count[x] = count.get(x, 0) + 1

    n = len(values)

    result = []
    for x in values:
        result.append(count[x] / n)

    return result