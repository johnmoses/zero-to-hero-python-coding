"""
Generator Functions

A generator uses 'yield' instead of 'return'. It produces values one at a
time (lazily) rather than building the whole list in memory at once.

Why use generators?
  - Memory efficient: only one value exists in memory at a time
  - Useful for large sequences (files, streams, infinite series)
"""

# Basic generator — yields values one by one
def count_up(n):
    for i in range(1, n + 1):
        yield i   # pauses here, resumes on next iteration

for num in count_up(5):
    print(num)


# Comparison: list vs generator memory usage
def list_squares(n):
    return [x ** 2 for x in range(n)]   # builds entire list in memory

def gen_squares(n):
    for x in range(n):
        yield x ** 2                     # produces one value at a time

print(list_squares(5))                   # [0, 1, 4, 9, 16]
print(list(gen_squares(5)))              # same output, less memory


# Infinite generator — impossible with a list
def integers_from(start=0):
    """Yields integers forever starting from start."""
    n = start
    while True:
        yield n
        n += 1

counter = integers_from(1)
print(next(counter))   # 1
print(next(counter))   # 2
print(next(counter))   # 3