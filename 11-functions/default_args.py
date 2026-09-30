"""
Default parameters or arguments
"""

def calculate_age (birth_year,current_year = 2021):
    age = current_year - birth_year
    return age
    
print('Age: ', calculate_age(1821))