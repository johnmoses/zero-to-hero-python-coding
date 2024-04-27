""" 
Intersect
"""

def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res 

s1 = 'scam'
s2 = 'spam'
intersect(s1, s2)