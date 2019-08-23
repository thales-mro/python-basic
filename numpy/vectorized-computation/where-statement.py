import numpy as np

print("Example with ternaries (slow, does not work for multidimensional arrays):")
xarray = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarray = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

result = [(x if c else y)
            for x, y, c in zip(xarray, yarray, cond)]
print(result)

print("Result with where statement")
result_where = np.where(cond, xarray, yarray)
print(result)