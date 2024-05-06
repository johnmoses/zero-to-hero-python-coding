s = 'Spam'

# Analysing
print('Analysing')
print(len(s))

# Indexing
print('Indexing')
print(s[0])           # index of first element
print(s[1])          # index of second element
print(s[-1])   # last item from end

# Slicing
print('Slicing')
print(s[1:3])      # slice from index 1 to 2
print(s[0:3])    # everything but the third index
print(s[:])               # everything as top-level

# Concatenate
print('Concatenate')
print(s + 'ss')

# Repeat
print(s * 2)

s = 'z' + s[1:]
print(s)

# Expanding to list
print('Expanding with list')
l = list(s)
print(l)

# Subset
print('Subsets')
fs = s.find('pa')
print(fs)

# Splitting
print('Splitting')
line = 'come,up,and,eat'
print(line.split(','))

# Formatting
print('Formatting')
print('A\nB\nC')            # line spacing
print('D\tE\tF')            # taps
print('WX\bYX')             
print('1\a2\a3\a4\a5\a6')
print('{0} and {1}'.format('Tom', 'Jerry'))

# Unicode and bytes
print('Unicode')
s = 'ni'
print(s.encode('ascii'))
print(s.encode('latin1'))
print(s.encode('utf8'))