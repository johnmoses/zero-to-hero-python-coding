"""
Making or Creating a Directory
"""

import os
directory = "d1"
parent_dir = "/Users/johnmoses/Workspace/zero-to-hero-python-coding/os"
path = os.path.join(parent_dir, directory)

os.mkdir(path)
print("Directory '% s' created" % directory)
