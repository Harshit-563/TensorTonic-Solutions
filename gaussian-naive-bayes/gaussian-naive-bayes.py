import math

def gaussian_naive_bayes(X_train: list, y_train: list, X_test: list) -> list:
    eps = 1e-9
    n = len(X_train)
    n_features = len(X_train[0])

    # Group samples by class
    classes = sorted(set(y_train))
    stats = {}

    for c in classes:
        class_samples = [X_train[i] for i in range(n) if y_train[i] == c]
        nc = len(class_samples)

        # Prior
        prior = nc / n

        means = []
        variances = []

        for j in range(n_features):
            values = [row[j] for row in class_samples]

            mean = sum(values) / nc
            var = sum((x - mean) ** 2 for x in values) / nc  # population variance

            means.append(mean)
            variances.append(var + eps)

        stats[c] = (prior, means, variances)

    predictions = []

    for x in X_test:
        best_class = None
        best_log_prob = float("-inf")

        for c in classes:
            prior, means, variances = stats[c]

            log_prob = math.log(prior)

            for j in range(n_features):
                mean = means[j]
                var = variances[j]

                log_prob += (
                    -0.5 * math.log(2 * math.pi * var)
                    - ((x[j] - mean) ** 2) / (2 * var)
                )

            if log_prob > best_log_prob:
                best_log_prob = log_prob
                best_class = c

        predictions.append(best_class)

    return predictions