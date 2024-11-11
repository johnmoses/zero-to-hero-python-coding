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
  "year" : 2004
}
child_2 = {
  "name" : "Tobias",
  "year" : 2007
}
child_3 = {
  "name" : "Linus",
  "year" : 2011
}

family = {
  "child1" : child_1,
  "child2" : child_2,
  "child3" : child_3
}

print(students)
print(cars)
print(employees)
print(family)

# Get properties
print(len(students))
print(type(students))