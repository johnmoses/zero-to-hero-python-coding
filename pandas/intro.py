"""
Pandas
"""

import pandas as pd 

# Create series with default index
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums)
print(s)


# create series with custom index
s = pd.Series(nums, index=[1, 2, 3, 4, 5])
print(s)

# Create series with string array and custom index
fruits = ['Orange','Banana','Mango']
fruits = pd.Series(fruits, index=[1, 2, 3])
print(fruits)