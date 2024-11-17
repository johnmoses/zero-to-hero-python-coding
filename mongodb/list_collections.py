""" 
List collections
"""

import pymongo

# Define client connection
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

# List collections
print(mydb.list_collection_names())

# List collection
collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")