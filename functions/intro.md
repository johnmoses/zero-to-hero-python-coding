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

## Lambda Functions

Lambda functions are small functions without names. They are like anonymous functions in JavaScript language. They are normally used inside other functions.

## Higher Order Functions

These type of functions return different functions based on the arguments

## Generator Functions

## Recursive Functions

These are functions that call itself.

## Functions as a parameter

Sometimes functions can be used as paramets to another function

## Functions as return values

Functions can be used as return value of another function

## Closures

Closure is a method of allowing a nested function to access the outer scope of the enclosing function. Practically, this is done by nesting a function inside another encapsulating function and then returning the inner function.

## Decorators

A decorator is a design pattern in Python that allows a user to add new functionality to ans existing object without changing its structure. We create a decorator function by first creating an outer function with an inner wrapper function
