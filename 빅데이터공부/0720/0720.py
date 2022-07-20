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

res = requests.get('https://davelee-fun.github.io/blog/crawl_html_css.html')
soup = BeautifulSoup(res.content, 'html.parser')
# section = soup.find('ul', id='hobby_course_list')
# items = soup.select('ul > li') # ul 바로 밑에 있는 li를 찾음
# items = soup.select('.course')
# items = soup.select('#start') # id 이름 찾으려면 # 붙이기
# items = soup.select('li.course.paid')
items = soup.select('tr')

# select_one = find
# select_all = find_all
for item in items:
    columns = item.select('td')
    row_str = ''
    for column in columns:
        row_str += ', ' + column.get_text()
    print(row_str[2:]) # 맨 앞의 , 제거