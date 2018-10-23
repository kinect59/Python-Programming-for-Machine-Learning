# Selecting Elements In An Array.

# Load library.
import numpy as np

# Create row vector.
vector = np.array([1, 2, 3, 4, 5, 6])

# Select second element.
print(vector[1])

# Create matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Select second colume, second row
print(matrix[1,1])

# Create tensor
tensor = np.array([
                    [[[1, 1], [1, 1]], [[2, 2], [2, 2]]],
                    [[[3, 3], [3, 3]], [[4, 4], [4, 4]]]
                  ])

# Select second element of each of the three dimensions
print(tensor[1, 1, 1])


