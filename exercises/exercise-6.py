import numpy as np
print("It calculates the log of array, if element is 0, it keeps that value.\nOriginal array:")
x = np.array([0, 2, 3, 5, 0, 7, 9, 0, 4])
indicies = x > 0
y = np.zeros(x.shape)
y[indicies] = np.log(x[indicies])
print("After operation:")
print(y)