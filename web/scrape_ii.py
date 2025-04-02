""" 
Scraping the web with beautiful soup
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://olympus.realpython.org/profiles/dionysus"

# Open the url
page = urlopen(url)

# Read contents
html = page.read().decode("utf-8")

# Create beautiful soup object
soup = BeautifulSoup(html, "html.parser")

# Get title
print('Title: ', soup.title)

# Get title text
print('Title text: ', soup.title.text)

# Get text
print('Text: ', soup.get_text())

# Find images
print('Image: ', soup.find_all('img'))