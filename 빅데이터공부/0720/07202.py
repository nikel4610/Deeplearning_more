import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

# request 라이브러리를 사용한 코드
res = requests.get('https://davelee-fun.github.io/')
soup = BeautifulSoup(res.content, 'html.parser')
data = soup.select('h4.card-text')
for item in data:
    print (item.get_text().strip())

# urlopen 라이브러리를 사용한 코드
res = urlopen('https://davelee-fun.github.io/')
soup = BeautifulSoup(res, 'html.parser')
data = soup.select('h4.card-text')
for item in data:
    print (item.get_text().strip())

# 결과는 똑같다