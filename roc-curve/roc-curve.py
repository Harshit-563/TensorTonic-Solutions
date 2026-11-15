import numpy as np

def roc_curve(y_true: list, y_score: list) -> dict:
    """
    Returns a dictionary with:
        - fpr: False Positive Rate values
        - tpr: True Positive Rate values
        - thresholds: decision thresholds
    """

    y_true = np.asarray(y_true)
    y_score = np.asarray(y_score)

    # Sort by score descending
    order = np.argsort(-y_score)
    y_true = y_true[order]
    y_score = y_score[order]

    P = np.sum(y_true == 1)
    N = np.sum(y_true == 0)

    tpr = [0.0]
    fpr = [0.0]
    thresholds = [np.inf]

    tp = fp = 0
    prev_score = None

    for i in range(len(y_score)):
        if prev_score is not None and y_score[i] != prev_score:
            tpr.append(tp / P if P else 0.0)
            fpr.append(fp / N if N else 0.0)
            thresholds.append(prev_score)

        if y_true[i] == 1:
            tp += 1
        else:
            fp += 1

        prev_score = y_score[i]

    # Final point
    tpr.append(tp / P if P else 0.0)
    fpr.append(fp / N if N else 0.0)
    thresholds.append(prev_score)
    fpr = np.asarray(fpr,dtype=float)
    tpr = np.asarray(tpr,dtype=float)
    thresholds = np.asarray(thresholds,dtype=float)
    return {
        "fpr": fpr,
        "tpr": tpr,
        "thresholds": thresholds,
    }