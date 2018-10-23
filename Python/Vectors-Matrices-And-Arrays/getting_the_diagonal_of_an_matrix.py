# Getting the diagonal of an matrix

# Load library
import numpy as np

# Create matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Getting the diagonal
print(matrix.diagonal())

# Calculate the tracre of the matrix
print(matrix.diagonal().sum())
