"""
Removing Directory
"""

import os 
directory = "d1"
parent = "/Users/johnmoses/Codings/zero-to-hero-coding/09_operating_systems/"
path = os.path.join(parent, directory) 
os.rmdir(path) 
