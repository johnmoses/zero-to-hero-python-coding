""" 
Data exploration
"""

import pandas as pd

df = pd.read_csv('weight-height.csv')

print(df.head())

print(df.tail())

print(df.shape) 

print(df.columns)