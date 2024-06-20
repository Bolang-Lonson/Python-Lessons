from bs4 import BeautifulSoup
import requests


try:
    response = requests.get('http://localhost:53156/')
    response.raise_for_status()
except requests.RequestException as e:
    print(str(e))

soup = BeautifulSoup(response.content, 'html.parser')
print(soup.contents)