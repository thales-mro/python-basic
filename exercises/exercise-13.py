import numpy as np

#multiply all items (xi * yi) of vector 
def compute_xi_yi(X, Y):
    return np.sum(X) * np.sum(Y)