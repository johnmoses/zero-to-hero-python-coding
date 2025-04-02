""" 
Write code to check if directory exists
"""

import os

path = "/Users/johnmoses/Workspace/zero-to-hero-coding/os"
print(os.path.isdir(path))
print(os.path.isfile(path))
print(os.path.exists(path))
print(os.path.exists("/Users/johnmoses/Workspace/zero-to-hero-coding/os/README.md"))
