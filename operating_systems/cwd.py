"""
Changing to Current Working Directory before
"""

import os 

def current_path(): 
    print("Current working directory before") 
    print(os.getcwd()) 

current_path() 
os.chdir('../') 
current_path() 
