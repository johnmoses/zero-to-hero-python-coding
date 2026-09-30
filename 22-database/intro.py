""" 
Database application with SQLite
"""

import sqlite3

# open a SQLite connection
# a database file called data.db will be created,
# if it does not exist
conn = sqlite3.connect('data.db')

# create a database cursor
cur = conn.cursor()

#
# Creating the table
#

# create the database table if it doesn't exist
table_schema = """
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT
);
"""
cur.execute(table_schema)

#
# Inserting to the database
#

# insert some hard-coded data
insert_query = """
INSERT INTO notes (name, description)
VALUES ('my first note', 'hi, this is the description');
"""
cur.execute(insert_query)

# save it in the database file
conn.commit()

#
# Querying the database
#

# query the database for ALL data in the notes table
cur.execute('SELECT * FROM notes;')

# print the result
result = cur.fetchall()
print(result)

# close the connection
conn.close()