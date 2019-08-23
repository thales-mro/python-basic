import numpy as np

print("Original array:")
x = np.array([6, 0, 0, 3, 2, 5, 6])
print(x, "\nWe want to remove all the elements that are equal to the biggest element.")
maxElement = np.max(x)
indicies = np.where(x == maxElement)
new_x = np.delete(x, indicies)
print("Cleaned array:\n", new_x)