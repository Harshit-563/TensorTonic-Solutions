def decision_tree_split(X: list, y: list) -> list:
    """
    Returns [best_feature_index, best_threshold].
    Uses Gini impurity to find the best split.
    """
    n_samples = len(X)
    n_features = len(X[0])

    def gini(labels):
        if not labels:
            return 0
        counts = {}
        for label in labels:
            counts[label] = counts.get(label, 0) + 1

        impurity = 1.0
        total = len(labels)

        for count in counts.values():
            p = count / total
            impurity -= p ** 2

        return impurity

    best_gini = float("inf")
    best_feature = -1
    best_threshold = None

    for feature in range(n_features):
        values = sorted(set(row[feature] for row in X))

        # midpoints between consecutive values
        thresholds = [
            (values[i] + values[i + 1]) / 2
            for i in range(len(values) - 1)
        ]

        for threshold in thresholds:
            left_y = []
            right_y = []

            for i in range(n_samples):
                if X[i][feature] <= threshold:
                    left_y.append(y[i])
                else:
                    right_y.append(y[i])

            if not left_y or not right_y:
                continue

            weighted_gini = (
                len(left_y) / n_samples * gini(left_y)
                + len(right_y) / n_samples * gini(right_y)
            )

            if weighted_gini < best_gini:
                best_gini = weighted_gini
                best_feature = feature
                best_threshold = threshold

    return [best_feature, best_threshold]