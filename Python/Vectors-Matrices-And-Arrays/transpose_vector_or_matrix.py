# Transpose a vector or a matrix.

# Load library.
import numpy as np

# Create a vector.
vector = np.array([1, 2, 3, 4, 5, 6])

# Create a matrix.
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Transpose vector.
print(vector.T) # Here it didn't transpose because vector is 1 dimensional.

# Transpose matrix.
print(matrix.T) # Columns <--> Rows
