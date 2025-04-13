"""
Removing Directory
"""

import os 
directory = "d1"
parent = "/Users/johnmoses/Workspace/zero-to-hero-python-coding/os"
path = os.path.join(parent, directory) 
os.rmdir(path) 
