""" 
Regular Expressions
"""

import re

# Search text
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

# Find text
x = re.findall("ai", txt)
print(x)

# Find all
x = re.findall("Portugal", txt)
print(x)

# Split
x = re.split("\s", txt)
print(x)

# Sub
x = re.sub("\s", "9", txt)
print(x)