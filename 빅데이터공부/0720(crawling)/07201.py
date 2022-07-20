import requests
from bs4 import BeautifulSoup

# for index in range(1, 10):
#     res = requests.get('https://davelee-fun.github.io/page' + str(index) + '/')
#     soup = BeautifulSoup(res.content, 'html.parser')
#     items = soup.select('span.post-date')
#     for item in items:
#         print (item.get_text().strip())

# res = requests.get('https://finance.naver.com/sise/')
# html =res.content.decode('euc-kr','replace') # 인코딩 해야 한글로 나옴
# soup = BeautifulSoup(html, 'html.parser')
# # a 태그이면서 href 속성 값이 특정한 값을 갖는 경우 탐색
# data = soup.select("#siselist_tab_0 > tr > td > a")
# for item in data:
#     print(item.get_text())

import requests
from bs4 import BeautifulSoup
res = requests.get('https://finance.naver.com/sise/')
html =res.content.decode('euc-kr','replace')
soup = BeautifulSoup(html, 'html.parser')
data = soup.select("div.rgt > ul.lst_major > li")

for item in data:
    # element 살펴보기
    print ("지수이름:", item.find('a').get_text(), "현재지수:", item.find('span').get_text(), item.find('em').get_text())
