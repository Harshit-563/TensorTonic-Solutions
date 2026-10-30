import numpy as np

def classification_metrics(y_true, y_pred,
                           average="macro",
                           pos_label=1):

    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    classes = np.unique(np.concatenate([y_true, y_pred]))

    # Per-class containers
    tps = []
    fps = []
    fns = []
    precisions = []
    recalls = []
    f1s = []
    supports = []

    for c in classes:
        true_mask = (y_true == c)
        pred_mask = (y_pred == c)

        tp = np.sum(true_mask & pred_mask)
        fp = np.sum(~true_mask & pred_mask)
        fn = np.sum(true_mask & ~pred_mask)

        support = np.sum(true_mask)

        precision = tp / (tp + fp) if tp + fp else 0.0
        recall = tp / (tp + fn) if tp + fn else 0.0

        f1 = (
            2 * precision * recall / (precision + recall)
            if precision + recall
            else 0.0
        )

        tps.append(tp)
        fps.append(fp)
        fns.append(fn)
        precisions.append(precision)
        recalls.append(recall)
        f1s.append(f1)
        supports.append(support)

    # Accuracy
    accuracy = np.mean(y_true == y_pred)

    # ---------- averaging ----------
    if average == "micro":
        tp = sum(tps)
        fp = sum(fps)
        fn = sum(fns)

        precision = tp / (tp + fp) if tp + fp else 0.0
        recall = tp / (tp + fn) if tp + fn else 0.0

        f1 = (
            2 * precision * recall / (precision + recall)
            if precision + recall
            else 0.0
        )

    elif average == "macro":
        precision = np.mean(precisions)
        recall = np.mean(recalls)
        f1 = np.mean(f1s)

    elif average == "weighted":
        total_support = sum(supports)

        precision = (
            np.sum(np.array(precisions) * np.array(supports))
            / total_support
            if total_support
            else 0.0
        )

        recall = (
            np.sum(np.array(recalls) * np.array(supports))
            / total_support
            if total_support
            else 0.0
        )

        f1 = (
            np.sum(np.array(f1s) * np.array(supports))
            / total_support
            if total_support
            else 0.0
        )

    elif average == "binary":
        true_mask = (y_true == pos_label)
        pred_mask = (y_pred == pos_label)

        tp = np.sum(true_mask & pred_mask)
        fp = np.sum(~true_mask & pred_mask)
        fn = np.sum(true_mask & ~pred_mask)

        precision = tp / (tp + fp) if tp + fp else 0.0
        recall = tp / (tp + fn) if tp + fn else 0.0

        f1 = (
            2 * precision * recall / (precision + recall)
            if precision + recall
            else 0.0
        )

    return {
        "accuracy": float(round(accuracy, 6)),
        "precision": float(round(precision, 6)),
        "recall": float(round(recall, 6)),
        "f1": float(round(f1, 6))
    }