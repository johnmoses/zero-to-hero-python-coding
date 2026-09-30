""" 
Dataframes from lists
"""

import pandas as pd 

# List of lists
data = [
    ['Joy', 'Finland', 'Helsink'], 
    ['David', 'UK', 'London'],
    ['John', 'Nigeria', 'Abuja']
]
df = pd.DataFrame(data, columns=['Names','Country','City'])
print(df)