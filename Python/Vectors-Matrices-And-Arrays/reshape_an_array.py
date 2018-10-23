# Reshape An Array

# Load library
import numpy as np

# Create a 4x3 matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [10, 11, 12]])

# There are total 4x3=12 elements.
# You can reshape the matrix into 2x6=12 elements
matrix = matrix.reshape(2, 6)

print(matrix)
