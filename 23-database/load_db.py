"""
Load in-memory database object from file
"""

dbfilename = 'people-db'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'

def load_db(dbfilename=dbfilename):
    dbfile = open(dbfilename)
    import sys
    sys.stdin = dbfile
    db = {}
    key = input()
    while key != ENDDB:
        rec = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value)
            field =input()
        db[key] = rec
        key = input()
    return db

if __name__ == '__main__':
    from intro import db
    load_db('people-db')
    
    # Display db
    for key in db:
        print(key, '=>\n ', db[key])