import requests
from bs4 import BeautifulSoup

res = requests.get('https://finance.naver.com/sise/')
html =res.content.decode('euc-kr','replace')
soup = BeautifulSoup(html, 'html.parser')
# a 태그이면서 href 속성 값이 특정한 값을 갖는 경우 탐색
data = soup.select("#popularItemList >li > a")
for item in data:
    print(item.get_text())
