a = 21
b = 10
print(a,b)

if (a == b):
    print('1: a equals b')
else:
    print("1: a not equals b")

if (a != b):
    print('2: a not equals b')
else:
    print('2: a equals b')

if (a < b):
    print('3: a is less than b')
else:
    print('3: a is not less than b')

if (a > b):
    print('4: a is greater than b')
else:
    print('4: a is not greater than b')

a,b = b,a
print(a,b)

if (a <= b):
    print('5: a is either less than or equal to b')
else:
    print('5: a is neither less than or equal to b')

if (a >= b):
    print('6: a is either less than or equal to b')
else:
    print('6: a is neither less than or equal to b')
