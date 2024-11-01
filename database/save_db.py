"""
Save in-memory database object to file
"""

dbfilename = 'people-db'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'

def save_db(db, dbfilename=dbfilename):
    dbfile = open(dbfilename, 'w')
    for key in db:
        print(key, file=dbfile)
        for (name, value) in db[key].items():
            print(name + RECSEP + repr(value), file=dbfile)
        print(ENDREC, file=dbfile)
    print(ENDDB, file=dbfile)
    dbfile.close()

if __name__ == '__main__':
    from intro import db
    save_db(db)