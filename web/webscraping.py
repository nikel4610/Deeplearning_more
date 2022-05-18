import requests
from bs4 import BeautifulSoup as bs

# 웹 페이지 가져오기
dangnReq = requests.get('https://www.daangn.com/hot_articles')
# print(dangnReq.text) -> 전체 페이지 내용 출력

dangnsoup = bs(dangnReq.content, 'html.parser')
dangnsoup.prettify()

mydata = dangnsoup.findAll('article', {'class': 'card-top'})
for string in mydata:
    print(string.get_text()) # 각 글의 제목, 가격, 위치, 관심도, 채팅 출력

