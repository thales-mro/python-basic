import numpy as np

m = np.array([[1, 0], [0, 2]])
print("Checking if matrix is lower triangular")
print(np.allclose(m, np.tril(m)))
print("Checking if matrix is upper triangular")
print(np.allclose(m, np.triu(m)))
print("Checking if matrix is diagonal triangular")
print(np.allclose(m, np.diag(np.diag(m))))

