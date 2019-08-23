import numpy as np

#apply threshold limits to M
def threshold(M, max_val, min_val):
    M[M > max_val] = max_val
    M[M < min_val] = min_val
    return M