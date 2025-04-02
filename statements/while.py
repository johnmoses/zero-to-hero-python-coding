""" 
while loops
"""

print('While loop with 1 step increment')
i = 1
while i < 6:
  print(i)
  i += 1

print('While loop with condition and break')
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

print('While loop with else')
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")