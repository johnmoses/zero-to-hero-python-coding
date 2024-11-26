""" 
Pandas Series
"""

import pandas as pd 
import numpy as np

# Create series with default index
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums)
print(s)


# create series with custom index
s = pd.Series(nums, index=[1, 2, 3, 4, 5])
print(s)

# Create series with string array and custom index
fruits = ['Orange','Banana','Mango']
s = pd.Series(fruits, index=[1, 2, 3])
print(s)

# Create series from a dictionary
data = {'name':'Joy','age':19,'school':'Saint Andrew'}
s = pd.Series(data)
print(s)

# Create series from linspace
# linspace(starting, end, items)
s = pd.Series(np.linspace(5, 20, 10))
print(s)