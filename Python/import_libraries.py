# Huy-Hieu PHAM, Ph.D. Fellow.
# Cerema Research Center & Toulouse Institute of Computer Science Research (IRIT)
# Paul Sabatier University - Toulouse III, Toulouse, France.
# Description: "Import module and packages in Python".
# Created date: Sep. 26, 2017

# Import math module.
import math

# Show all functions in math module.
content = dir(math)

# Using functions in math module.
math.sqrt(25)

# Import a specific function.
from math import sqrt
sqrt(25)

# Import multiple functions at once.
from math import floor, sin, cos, tan, acos, asin, atan
floor(1.2)
sin(1)
cos(1)
tan(1)
acos(1)
asin(1)
atan(1)

# Import OS function for working with your system.
import os

# Execute a shell command.
os.system()  

# Get the users enviroments.
os.environ()  

# Return the current working directory.
os.getcwd()  

# Return information identifying the current operating system.
os.uname()    

# Change the root directory of the current process to path.
os.chroot(path)   

# Return a list of the entries in the directory given by path.
os.listdir(path) 

# Create a directory named path with numeric mode mode.
os.mkdir(path)    

# Recursive directory creation function.
os.makedirs(path)  

#Remove (delete) the file path.
os.remove(path)    

# Import an library as an alias.
import numpy as np


