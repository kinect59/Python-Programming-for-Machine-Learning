# Create a sparse matrix

# Load library
import numpy as np
from scipy import sparse

# Create a matrix
matrix = np.array([[1, 2],
                  [3, 4],
                  [5, 6]])

# Create compressed sparse row (CSR) matrix

matrix_sparse = sparse.csr_matrix(matrix)

print(matrix_sparse)
