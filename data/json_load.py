""" 
JSON
JSON is text, written with JavaScript object notation
"""

import json

x =  '{ "name":"Hiy", "age":40, "city":"London"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
