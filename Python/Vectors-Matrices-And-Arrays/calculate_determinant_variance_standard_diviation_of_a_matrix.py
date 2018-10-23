# Calculate the determinant of a matrix

# Load library
import numpy as np

# Create matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Calculate determinant of matrix
print(np.linalg.det(matrix))

# Calculate the mean
print(np.mean(matrix))

# Calculate Variance
print(np.var(matrix))

# Calculate Standard Deviation
print(np.std(matrix))
