""" 
List databases
"""

import pymongo

# Define client connection
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# List databases
print(myclient.list_database_names())

# Find specific db
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")