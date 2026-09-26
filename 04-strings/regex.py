""" 
Regular Expressions
"""

import re

txt = "The rain in Spain"

# Search text
x = re.search("^The.*Spain$", txt)
print('Search: ', x)

x = re.search('rain', txt, re.I)
print('Search 2: ', x)

# Find text
x = re.findall("ai", txt)
print('Find all: ', x)

# Find all
x = re.findall("Portugal", txt)
print('Find all 2: ', x)

# Split
x = re.split("\s", txt)
print('Split text: ', x)

# Replacing a substring
x = re.sub("\s", "9", txt)
print('Replace: ', x)

x = re.sub("%", "", txt)
print('Replace 2: ', x)