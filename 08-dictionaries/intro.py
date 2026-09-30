""" 
Dictionaries
"""

# Create dictionaries
students = {'name': 'Edy', 'age': 26}
cars = {
  "brand": "Ford",
  "model": "Edge",
  "year": 2008
}
employees = dict(name = "John", age = 36, country = "Norway")

child_1 = {
  "name" : "Emil",
  "date_of_birth" : 2004,
  "address": {
    "street": "Joy street",
    "school": "Baptist High School",
  },
  "skills": ['Footbal','Singing'],
}
child_2 = {
  "name" : "Tobias",
  "date_of_birth" : 2007
}
child_3 = {
  "name" : "Linus",
  "date_of_birth" : 2011
}

family = {
  "child1" : child_1,
  "child2" : child_2,
  "child3" : child_3
}

print('Students: ', students)
print('Cars: ', cars)
print('Employees: ', employees)
print('Family: ', family)

# Get properties
print('Students length: ',len(students))
print('Students type: ', type(students))

# Get value from key
print('Key value: ', students['name'])

# Get keys
print('Students keys: ', students.keys())

# Get values
print('Students values: ', students.values())

# Get items
print('Students items: ', students.items())