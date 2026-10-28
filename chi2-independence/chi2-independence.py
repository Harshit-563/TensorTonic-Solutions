import numpy as np

def chi2_independence(C: list) -> dict:
    """
    Returns a dictionary with chi2 and expected.
    """
    C = np.asarray(C,dtype=float)
    column_totals = np.sum(C,axis=0)
    row_totals = np.sum(C,axis=1)
    total = np.sum(C)
    expected =  np.outer(row_totals, column_totals) / total
    a = np.sum((C - expected) ** 2 / expected)
    return {"chi2":float(a),"expected":expected}
    