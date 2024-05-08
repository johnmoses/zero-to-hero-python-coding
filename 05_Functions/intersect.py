""" 
Intersect sequences with different inputs,
to demonstrate polymorphism 
"""

def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res 

s1 = 'scam'
s2 = 'spam'
s3 = [1,2,3]
s4 = [3,4,5]
print(intersect(s1, s2))
print(intersect(s3, s4))