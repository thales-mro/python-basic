import numpy as np

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print("Original array with repeated elements:", names)

print("Array with unique elements (works for int elements too):", np.unique(names))

print("Function np.in1d tests membership of the values in one array in another, returning boolean array")
print("Array to be tested:")
values = np.array([6, 0, 0, 3, 2, 5, 6])
print(values)
print("Values to be tested with:")
tarray = np.array([2, 3, 6])
print(np.in1d(values, tarray))