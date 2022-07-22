from bs4 import BeautifulSoup

data_file = open('빅데이터공부/0722/users.xml', 'r', encoding='utf-8-sig')
soup = BeautifulSoup(data_file, 'lxml')

users = soup.select('user')

for user in users:
    name = user.select_one('name')
    print('이름:', name.text)
    age = user.select_one('age')
    print('나이:', age.text)
    