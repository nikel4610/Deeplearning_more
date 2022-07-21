import openpyxl
import requests
from bs4 import BeautifulSoup


# excel_file = openpyxl.Workbook()
# excel_sheet = excel_file.active

# # 엑셀 내용 추가
# excel_sheet.append(['data1', 'data2', 'data3'])

# # 이름 바꾸기
# # excel_sheet.title = '리포트'

# # 저장
# excel_file.save('tmp.xlsx')
# excel_file.close()

def write_excel_template(filename, sheetname, listdata):
    excel_file = openpyxl.Workbook()
    excel_sheet = excel_file.active
    # 글자 셀 길이 조절
    excel_sheet.column_dimensions['A'].width = 80
    excel_sheet.column_dimensions['B'].width = 20

    if sheetname != '':
        excel_sheet.title = sheetname

    # 한 줄 씩 집어넣는다
    for item in listdata:
        excel_sheet.append(item)

    excel_file.save(filename)
    excel_file.close()

product_lists = list()

for page_num in range(10):
    if page_num == 0:
        res = requests.get('https://davelee-fun.github.io/')
    else:
        res = requests.get('https://davelee-fun.github.io/page' + str(page_num + 1))
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.select('div.card')

# for 안에 for 넣는거 주의하기
# 크롤링한 데이터를 한번 더 크롤링해서 저장한다
    for item in data:
        # > 랑 빈칸이랑 상관없음
        product_name = item.select_one('div.card-body > h4')
        product_date = item.select_one('div.wrapfooter span.post-date')
        product_info = [product_name.get_text().strip(), product_date.get_text()]
        product_lists.append(product_info)

write_excel_template('tmp.xlsx', '상품정보', product_lists)
