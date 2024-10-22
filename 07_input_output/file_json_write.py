""" 
Write to JSON file 
"""
import json

data = {
    'greeting': 0,
    'thanks': 1,
    'goodbye': 2
 }

with open('labels.json', 'w') as file:
    json_string = json.dumps(data, default=lambda o: o.__dict__, sort_keys=True, indent=2)
    file.write(json_string)