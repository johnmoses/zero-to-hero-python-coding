""" 
Getting requests from external API
"""
import requests

url = 'https://jsonplaceholder.typicode.com/todos/1'

# Use the requests get method to fetch the data from url
response = requests.get(url)

# Check the status
status = response.status_code
print(status) # 200 means the fetching was successful