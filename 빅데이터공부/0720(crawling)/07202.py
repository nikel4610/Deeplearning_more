import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

# # request 라이브러리를 사용한 코드
# res = requests.get('https://davelee-fun.github.io/')
# soup = BeautifulSoup(res.content, 'html.parser')
# data = soup.select('h4.card-text')
# for item in data:
#     print (item.get_text().strip())

# # urlopen 라이브러리를 사용한 코드
# res = urlopen('https://davelee-fun.github.io/')
# soup = BeautifulSoup(res, 'html.parser')
# data = soup.select('h4.card-text')
# for item in data:
#     print (item.get_text().strip())

# # 결과는 똑같다

# # 페이지가 없는 경우 확인
# res = requests.get('https://davelee-fun.github.io/xxx')
# if res.status_code != 200:
#     print ('페이지 없음')
# else:
#     soup = BeautifulSoup(res.content, 'html.parser')
#     data = soup.select('h4.card-text')
#     for item in data:
#         print (item.get_text())

# 여러 페이지 크롤링 방법
# 사용할 때 주의하기
for page_num in range(10):
    if page_num == 0:
        res = requests.get('https://davelee-fun.github.io/')
    else:
        res = requests.get('https://davelee-fun.github.io/page' + str(page_num + 1))
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.select('h4.card-text')
    for item in data:
        print (item.get_text().strip())
