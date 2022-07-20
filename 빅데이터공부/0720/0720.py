import requests
from bs4 import BeautifulSoup

# html = "<html> \
#     <body> \
#         <h1 id = 'title'[1]크롤링이란?</h1> \
#         <p class = 'cssstyle'>웹페이지에서 필요한 데이터를 추출하는 것</p> \
#             <p id='body' align='center'>파이썬을 중심으로 다양한 웹크롤링 기술 발달</p> \
#             </body> \
#                 </html>"
# soup = BeautifulSoup(html, 'html.parser')
# data = soup.find(id='body') # p를 넣으면 p에 해당하는 태그 전체가 나옴, 한번만
# # 전부 찾고 싶으면 find_all() 사용
# # data2 = soup.find_all('p')
# # for paragraph in data2:
# #     print(paragraph.get_text())
# print(data)
# print(data.string)
# print(data.get_text())
# # print(data2)

# res = requests.get('https://v.media.daum.net/v/20170615203441266')
# soup = BeautifulSoup(res.content, 'html.parser')
# # mydata = soup.find('h3', 'tit_view')
# # print(mydata.get_text())

# data2 = soup.find_all('span', 'txt_info')
# for item in data2:
#     print(item.get_text())
# print(data2[1].get_text()) # [번호]를 넣어서 해당 번호의 문장 출력

# data3 = soup.find('div', 'layer_util layer_summary')
# print(data3.get_text())

res = requests.get('https://davelee-fun.github.io/blog/crawl_test')
soup = BeautifulSoup(res.content, 'html.parser')
section = soup.find('ul', id='hobby_course_list')

titles = soup.find_all('li', 'course')
for index, title in enumerate(titles):
    print(str(index+1) + '.', title.get_text().split('-')[1].split('[')[0].strip())