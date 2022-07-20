import requests
from bs4 import BeautifulSoup

# for index in range(1, 10):
#     res = requests.get('https://davelee-fun.github.io/page' + str(index) + '/')
#     soup = BeautifulSoup(res.content, 'html.parser')
#     items = soup.select('span.post-date')
#     for item in items:
#         print (item.get_text().strip())

res = requests.get('https://finance.naver.com/sise/')
html =res.content.decode('euc-kr','replace')
soup = BeautifulSoup(html, 'html.parser')
# a 태그이면서 href 속성 값이 특정한 값을 갖는 경우 탐색
data = soup.select("#siselist_tab_0 > tr > td > a")
for item in data:
    print(item.get_text())