"""  
Load content from pickle
"""

import pickle

file = open('datafile.pkl', 'rb')
content = pickle.load(file)
print(content)