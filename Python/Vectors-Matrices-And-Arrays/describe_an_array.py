# Describe An Array

# Load library
import numpy as np

# Create matrix
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

# View number of rows and columns
print(matrix.shape)

# View number of elements
print(matrix.size)

# View number of dimensions

print(matrix.ndim)

# Return maximum element
print(np.max(matrix))

# Return minimum element
print(np.min(matrix))

# Find the maximum element in each column
print(np.max(matrix, axis=0))

# Find the maximum element in each row
print(np.max(matrix, axis=1))
