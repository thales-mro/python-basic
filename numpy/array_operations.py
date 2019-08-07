'''
np.add()
np.subtract()
np.multiply()
np.divide()
np.remainder()

a.sum() -> array-wise sum
a.min() -> array-wise min
a.max(axis=0) -> maximum value of array (axis = 0 -> vertically)
a.cumsum(axis=1) -> cumulative sum of elements  starting from 0 (axis = 1 -> horizontally)
a.cumprod() -> cumulative product of the elements of array starting from 1
a.mean()
a.median()
a.corrcoef() -> correlation coefficient
np.var() -> variance
np.std(a) -> standard deviation

'''
import numpy as np

x = np.arange(12).reshape((3, 4))
print(x)
print("Horizontal sum:")
print(x.sum(axis=1))
print("Vertical sum;")
print(x.sum(axis=0))

