"""
Reading from input files
"""

file = open('data.txt')
lines = file.readlines()
for line in lines:
    print(line, end='')

# Short form
# open('data.txt').readlines()

# lines = [line.strip() for line in open('data.txt')]

file.close()