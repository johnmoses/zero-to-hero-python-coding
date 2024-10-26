"""
Making or Creating a Directory
"""

import os
directory = "d1"
parent_dir = "/Users/johnmoses/Codings/zero-to-hero-coding/09_operating_systems"
path = os.path.join(parent_dir, directory)

os.mkdir(path)
print("Directory '% s' created" % directory)
