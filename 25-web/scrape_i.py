""" 
Scraping the web
"""
import requests
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"

# Use the requests get method to fetch the data from url
response = requests.get(url)

# Check the status
status = response.status_code
print(status) # 200 means the fetching was successful

# Open url
page = urlopen(url)
print(page)

# Read and display web page contents
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)