import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Real_analysis'

response = requests.get(url)

if response.status_code == 200:
    print("Successfully fetched the webpage!")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

