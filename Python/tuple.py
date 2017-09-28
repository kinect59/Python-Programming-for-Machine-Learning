# Huy-Hieu PHAM, Ph.D. Fellow.
# Cerema Research Center & Toulouse Institute of Computer Science Research (IRIT)
# Paul Sabatier University - Toulouse III, Toulouse, France.
# Description: " Using Tuple in Python".
# Created date: Sep. 28, 2017


# Tuple likes list, but it can contain multiple data types.
# Note that the elements of a tuple cannot be modified.

# Create a tuple.
digits = (1, 2, 'three')

# Examine a tuple.
digits[1]                 # Returns 2
len(digits)               # Returns 3
digits.count(0)           # Examines how many element that is equal 0. Returns 0.
digits.index(1)           # Returns the index of the element that is equal 1. 

# Concatenate tuples.
digits = digits + (4, 5)  # Returns (1, 2, 'three', 4, 5)

# Repeate a tuple.
digits = digits * 2     # Returns (1, 2, 'three', 4, 5, 1, 2, 'three', 4, 5,)





  

