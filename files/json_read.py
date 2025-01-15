""" 
Read a JSON file 
"""
import json

with open('labels.json') as file:
    labels = json.load(file)
    print(labels)