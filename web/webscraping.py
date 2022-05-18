import requests
from bs4 import BeautifulSoup as bs

# 웹 페이지 가져오기
dangnReq = requests.get('https://www.daangn.com/hot_articles')
# print(dangnReq.text) -> 전체 페이지 내용 출력

dangnsoup = bs(dangnReq.content, 'html.parser')
dangnsoup.prettify()

sale = dangnsoup.findAll('h2', 'card-title')
price = dangnsoup.findAll('div', 'card-price')
address = dangnsoup.findAll('div', 'card-region-name')

prodName = []
prodPrice = []
prodAddress = []

for name in sale:
    prodName.append(name.text.strip())

for price in price:
    prodPrice.append(price.text.strip())

for address in address:
    prodAddress.append(address.text.strip())

for i in range(len(prodName)):
    print(prodName[i], prodPrice[i], prodAddress[i])

