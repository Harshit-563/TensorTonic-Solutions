def f1_micro(y_true: list[int], y_pred: list[int]) -> float:
    """
    Returns the micro-averaged F1 score as a Python float rounded to four decimals.
    """
    # Write code here
    a = sum(actual == predicted for actual, predicted in zip(y_true, y_pred)) 
    b = len(y_pred) - a
    return 2 * a/(2 *a + 2*b)
    pass