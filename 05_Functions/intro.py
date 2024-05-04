"""
Functions
"""
# function definition
def times(x, y):
    return x * y 

# function call
print(times(2,3))

# saving result to another object
c = times(3, 4)
print(c)

# use various types as input parameters
print(times('ne', 3))

def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res 

s1 = 'scam'
s2 = 'spam'
print(intersect(s1, s2))