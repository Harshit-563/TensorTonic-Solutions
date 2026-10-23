from collections import Counter

def random_forest_vote(predictions: list) -> list:
    result = []

    for sample_votes in zip(*predictions):
        counts = Counter(sample_votes)
        max_count = max(counts.values())

        # choose the smallest label among those with max votes
        winner = min(label for label, cnt in counts.items()
                     if cnt == max_count)

        result.append(winner)

    return result