""" 
NumPy
"""
import numpy as np

# Python list
lst_1 = [1,2,3,4,5]
print('Python list 1: ', lst_1)

# Multi-dimensional list
lst_22 = [[0,1,2], [3,4,5], [6,7,8]]
print('Python list 2: ', lst_22)

# Boolean arrays
bool_np = np.array([0, -1, 0, 0], dtype=bool)
print('Boolean: ', bool_np)

# Numpy list from python list
numpy_list = np.array(lst_1)
print('List: ', numpy_list)

# Numpy float array from python list
numpy_floats_list = np.array(lst_1, dtype=float)
print('Floats: ', numpy_floats_list)

# Shape of array
print('Floats shape: ', numpy_floats_list.shape)

# Data type of array
print('Type: ', numpy_floats_list.dtype)

# Size of array
print('Size: ', numpy_floats_list.size)