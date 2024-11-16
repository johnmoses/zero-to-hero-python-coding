""" 
Dump JSON
"""

import json

# a Python object (dict):
x = {
  "name": "Joy",
  "age": 40,
  "city": "London"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)