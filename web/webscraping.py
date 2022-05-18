import requests
from bs4 import BeautifulSoup as bs

# 웹 페이지 가져오기
dangnReq = requests.get('https://www.daangn.com/hot_articles')
# print(dangnReq.text) -> 전체 페이지 내용 출력

dangnsoup = bs(dangnReq.content, 'html.parser')
dangnsoup.prettify()

