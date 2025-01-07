""" 
range
"""

# Using a range
range(0, 5)
list(range(5))

for var in list(range(5)):
    print (var)

# Starting with a paramater
print('Using parameter')
for x in range(2, 6):
  print(x)

# Specifying incrementation factor
print('Using increment factor')
for x in range(2, 30, 3):
  print(x)

# Using else
print('Using conditional else')
for x in range(6):
    if x == 3: break
    print(x)
else:
  print("Finally finished!")