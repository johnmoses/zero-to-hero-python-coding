""" 
Write multiple lines
"""

file = open('data.txt','w')
file.writelines(
    [
        'Hello file world\n', 
        'How are you doing?\n', 
        'Hope fine?\n', 
        'Bye\n'
    ]
)
file.close()