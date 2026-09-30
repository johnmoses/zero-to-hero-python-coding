"""
Raising Exceptions

Use 'raise' to trigger an exception deliberately when your code detects
an invalid state. This gives callers a clear error instead of letting
the program silently produce wrong results.
"""

# Raise a built-in exception with a descriptive message
def set_age(age):
    if age < 0:
        raise ValueError(f"Age cannot be negative, got {age}")
    if not isinstance(age, int):
        raise TypeError(f"Age must be an int, got {type(age).__name__}")
    return age

try:
    set_age(-1)
except ValueError as e:
    print(f"ValueError: {e}")

try:
    set_age("thirty")
except TypeError as e:
    print(f"TypeError: {e}")


# Re-raising — catch, log, then let it propagate
def load_config(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        print(f"Config file not found: {path}")
        raise   # re-raise the original exception unchanged

try:
    load_config("missing.cfg")
except FileNotFoundError:
    print("Handled by caller")