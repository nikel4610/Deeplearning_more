import requests
from bs4 import BeautifulSoup

res = requests.get('https://v.media.daum.net/v/20170615203441266')
soup = BeautifulSoup(res.content, 'html.parser')
mydata = soup.find('title')
print(mydata.get_text())