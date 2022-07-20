import requests
from bs4 import BeautifulSoup

html = "<html> \
    <body> \
        <h1 id = 'title'[1]크롤링이란?</h1> \
        <p class = 'cssstyle'>웹페이지에서 필요한 데이터를 추출하는 것</p> \
            <p id='body' align='center'>파이썬을 중심으로 다양한 웹크롤링 기술 발달</p> \
            </body> \
                </html>"
soup = BeautifulSoup(html, 'html.parser')
data = soup.find(id='body') # p를 넣으면 p에 해당하는 태그 전체가 나옴, 한번만
# 전부 찾고 싶으면 find_all() 사용
# data2 = soup.find_all('p')
# for paragraph in data2:
#     print(paragraph.get_text())
print(data)
print(data.string)
print(data.get_text())
# print(data2)