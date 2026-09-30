""" 
Creating dataframe
"""

import pandas as pd

# Creating dataframe from list of list
data = [
    ['Joy', 'US', 'California'], 
    ['David', 'UK', 'London'],
    ['John', 'Nigeria', 'Abuja']
]
df = pd.DataFrame(data, columns=['Names','Country','City'])
print(df)

# Creating dataframe from dictionary
data = {
    'Name': ['Joy', 'David', 'John'], 
    'Country':['Us', 'UK', 'Nigeria'], 
    'City': ['California', 'London', 'Abuja']}
df = pd.DataFrame(data)
print(df)

# Creating from list of dictionaries
data = [
    {'Name': 'Joy', 'Country': 'US', 'City': 'California'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Nigeria', 'City': 'Abuja'}]
df = pd.DataFrame(data)
print(df)