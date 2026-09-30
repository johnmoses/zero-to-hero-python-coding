""" 
Reading Coma Separated Values (CSV)

Create a file 'data.csv' and add some content
"name","country","city","skills"
"Asabeneh","Finland","Helsinki","JavaScript"
"""

import csv

with open('data.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names: {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]}, {row[1]}, {row[2]}')
            line_count += 1
    print(f'Number of lines: {line_count}')