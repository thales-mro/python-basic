import numpy as np

a = np.array([[2.0, 4.0, 5.0], [-3.0, 8.0, -7.0], [0.0, 6.0, 4.0]])
mask = a > 0
print("Elements from A greater than 0")
print(mask)
print("Sum column elements that are grater than zero")
col_sums = np.sum(a*mask, axis = 0)
counts = np.sum(mask, axis = 0)
print(counts)
print("Calculates the mean of elements grater than zero in a by column")
means = col_sums/counts
print(means)