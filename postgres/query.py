""" 
Query data
"""

import psycopg2
def get_connection():
    try:
        return psycopg2.connect(
            database="postgres",
            user="postgres",
            password="password",
            host="127.0.0.1",
            port=5432,
        )
    except:
        return False

conn = get_connection()

# Create cursor
curr = conn.cursor()

# Execute query
curr.execute("SELECT * FROM students;")

# Fetch one row
data1 = curr.fetchone()

# Fetch many rows
data2 = curr.fetchmany()

# Fetch all rows
data3 = curr.fetchall()

# Print results
for row in data:
    print(row)

# Close connection
conn.close()