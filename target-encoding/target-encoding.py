def target_encoding(categories: list, targets: list) -> list:
    """
    Returns each category replaced by its mean target.
    """
    # Write code here
    if len(categories) != len(targets) or len(categories) == 0:
        raise ValueError("Categories and targets must have the same non-zero length")
    
    # Step 1: Build sum and count for each category
    sums = {}
    counts = {}
    for cat, val in zip(categories, targets):
        sums[cat] = sums.get(cat, 0) + val
        counts[cat] = counts.get(cat, 0) + 1
    
    # Step 2: Compute mean for each category
    means = {cat: sums[cat] / counts[cat] for cat in sums}
    
    # Step 3: Map categories to their mean values
    return [float(means[cat]) for cat in categories]