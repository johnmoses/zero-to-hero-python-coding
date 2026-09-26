"""
Deleting or removing a file
"""

import os

# Delete gracefully
if os.path.exists('data_1.txt'):
    os.remove('data_1.txt')
else:
    print('File does not exist')