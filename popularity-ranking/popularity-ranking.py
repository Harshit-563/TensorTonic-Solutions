def popularity_ranking(items: list, min_votes: int, global_mean: float) -> list:
    """
    Returns the weighted rating for every item.
    """
    wr = []
    for i in range(len(items)):
        a = items[i][1] + min_votes
        wr.append((items[i][0]*items[i][1] + min_votes*global_mean)/a)
    return wr    
        