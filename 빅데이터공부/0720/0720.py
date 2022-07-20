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
data = soup.find('h1')
print(data)
print(data.spring)
print(data.get_text())