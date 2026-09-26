"""  
Dump content to pickle
"""

import pickle

D = {'a': 1, 'b': 2}
F = open('datafile.pkl', 'wb')
pickle.dump(D, F)
F.close