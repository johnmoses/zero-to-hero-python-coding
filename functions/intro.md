# Functions

Function is a reuseable block of code that groups a set of statements so they can be executed more than once in the computer. They help in code reuse that makes the program code more readable and useful.

Python comes loaded with lots of built-in functions. However it also provides enough room for custom functions that we can add to extend the functionality of the computer.

Functions can be created using `def` or `lambda` keywords. Scope visibility could be `global` or `nonlocal`. They can send back results to the caller by `return` or `yield` keywords.

```py
# function definition
def times(x, y):
    return x * y 

# function call
times(2, 3)
```

```py
# saving result to another object
c = times(3, 4)
print(c)
```

## Polymorphism

Here the functions does different things depending on the supplied arguments. The times function does multiplication in one and repetition in another. Polymorphism is also called `duck typing` as compared to how a duck quacks

## Scope

A variable is only available from inside the region it is created

Local: A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

Global: A variable created in the main body of the Python code is a global variable and belongs to the global scope.
Global variables are available from within any scope, global and local.
