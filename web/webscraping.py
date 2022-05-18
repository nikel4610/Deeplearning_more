import requests
from bs4 import BeautifulSoup as bs

# 웹 페이지 가져오기
dangnReq = requests.get('https://www.daangn.com/hot_articles')
# print(dangnReq.text) -> 전체 페이지 내용 출력

dangnsoup = bs(dangnReq.content, 'html.parser')
dangnsoup.prettify()

sale = dangnsoup.findAll('h2', 'card-title')
for productName in sale:
    print(productName.text.strip()) # 각 글의 제목 출력

price = dangnsoup.findAll('div', 'card-price')
for productPrice in price:
    print(productPrice.text.strip()) # 각 글의 가격 출력

