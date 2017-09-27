# Huy-Hieu PHAM, Ph.D. Fellow.
# Cerema Research Center & Toulouse Institute of Computer Science Research (IRIT).
# Paul Sabatier University - Toulouse III, Toulouse, France.
# Description: "Using lists in Python".
# Created date: Sep. 27, 2017.


# Two ways to create an empty list.
empty_list = []
empty_list = list()

# Create a list with its data.
simpsons = ['homer', 'marge', 'bart']

# Examine a list.
simpsons[0]             # Print the first element.
len(simpsons)           # Check the length of the list.

# Modify the content of a list.
simpsons[0] = 'krusty'  # Replace the first element.
del simpsons[0]         # Delete the first element.
simpsons.insert(0,'maggie')                   # Insert element, the total element plus to 1.
simpsons.extend(['extend1', 'extend2'])       # Extend more elements to the list.

# Concatenate lists.
neighbors = simpsons + ['ned', 'rod', 'todd']

# Find elements in a list.
simpsons.count('lisa')                        # Counts the number of element "lisa".
simpsons.index('itchy')                       # Returns the index of the element.

# List slicing.
weekdays = ['mon','tues','wed','thurs','fri']
weekdays[0]                                   # Returns the element 0.
weekdays[0:3]                                 # Returns 0,1,2.
weekdays[:3]                                  # Returns 0,1,2.
weekdays[3:]                                  # Returns 3,4
weekdays[-1]                                  # Return the last element.
weekdays[::2]                                 # Return 2nd element: 0,2,4


# Return the list backwards.
list(reversed(weekdays))

# Copy a list.
list_1 = ['one','two']
list_2 = list_1.copy()
list_2 = list_1[:]
list_2 = list(list_1)


