# Initialize data to be stored in files, pickles and shelves

# Records
joy = {'name': 'Joy Island', 'age': 42, 'pay':30000, 'job': 'dev'}
mic = {'name': 'Mic One', 'age': 44, 'pay':50000, 'job': 'pro'}
tim = {'name': 'Tim Love', 'age': 46, 'pay':0, 'job': None}

# Database
db = {}
db['joy'] = joy
db['mic'] = mic
db['tim'] = tim

if __name__ == '__main__':
    for key in db:
        print(key, '=>\n ', db[key])