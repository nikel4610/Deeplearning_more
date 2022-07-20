import requests
from bs4 import BeautifulSoup

for index in range(1, 10):
    res = requests.get('https://davelee-fun.github.io/page' + str(index) + '/')
    soup = BeautifulSoup(res.content, 'html.parser')
    items = soup.select('div.card-body > h4')
    for item in items:
        print (item.get_text().strip())
