""" 
Global variable scope
"""
x = 300 # Global variable

def func_a():
  x = 200
  print(x)

func_a()

print(x)

# Using global keyword
def func_b():
    global x
    x = 300

func_a()

print(x)

# Using 'nonlocal' keyword
def func_c():
    x = "Jim"
    def func_d():
        nonlocal x
        x = "Tim"
    func_d()
    return x

print(func_c())