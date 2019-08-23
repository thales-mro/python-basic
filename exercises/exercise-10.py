import numpy as np

x = np.linspace(-2., 2., 5)
print(x)
y = np.where(x <= 0.5, x**2, -x)
print(y)