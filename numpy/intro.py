""" 
NumPy
"""
import numpy as np

# Python list
lst1 = [1,2,3,4,5]
print(lst1)

# Two dimensional list
lst2 = [[0,1,2], [3,4,5], [6,7,8]]
print(lst2)

# Numpy list from python list
numpy_list = np.array(lst1)
print(numpy_list)

# Numpy float array from python list
numy_floats_list = np.array(lst1, dtype=float)
print(numy_floats_list)