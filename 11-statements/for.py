"""
For Loops
"""

# Looping through a list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Looping through a string
for x in "banana":
  print(x)

# Loop with break
for x in fruits:
  print(x)
  if x == "banana":
    break

# Loop with 'continue'
for x in fruits:
    if x == "banana":
        continue
    print(x)

# Using else
for x in range(6):
  print(x)
else:
  print("Finally finished!")

# Using pass
for x in [0, 1, 2]:
  pass