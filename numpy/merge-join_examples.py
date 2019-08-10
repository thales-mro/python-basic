import numpy as np

array1d = np.array([1, 2, 3, 4])
print(array1d)

x = np.array([5, 6, 7, 8])
print("Concatenating 2 1d-arrays")
print(np.concatenate((array1d, x)))

print("Stack arrays row-wise:")
array2d = np.array([[6, 7, 8, 9], [4, 3, 2, 1]])
print(np.vstack((array1d, array2d)))

print("Stack arrays column-wise:")
print(np.column_stack((array2d, np.array([[1],[2]]))))

print("Split 2-d array horizontally at the 2nd index:")
print(np.hsplit(array2d, 2))

print("Split 2-d array vertically at 2nd index:")
print(np.vsplit(array2d, 2))

