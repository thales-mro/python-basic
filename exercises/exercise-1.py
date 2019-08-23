import numpy as np

a = np.full((5, 10), 7)
print(a)

print("or")

b = np.ones((5, 10))*7

print("or (non-vectorized, slower)")

c = np.empty([5, 10])
for i in range(5):
    for j in range(10):
        c[i][j] = 7
print(c)