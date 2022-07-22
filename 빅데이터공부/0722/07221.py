import requests
from bs4 import BeautifulSoup
import openpyxl

def write_excel_template(filename, sheetname, listdata):
    excel_file = openpyxl.Workbook()
    excel_sheet = excel_file.active
    # 글자 셀 길이 조절
    excel_sheet.column_dimensions['A'].width = 120
    excel_sheet.column_dimensions['B'].width = 20
    excel_sheet.column_dimensions['C'].width = 40

    if sheetname != '':
        excel_sheet.title = sheetname

    # 한 줄 씩 집어넣는다
    for item in listdata:
        excel_sheet.append(item)

    excel_file.save(filename)
    excel_file.close()

product_lists = list()

res = requests.get('http://corners.gmarket.co.kr/Bestsellers?viewType=G&groupCode=G06')
soup = BeautifulSoup(res.content, 'html.parser')
bestlists = soup.select('div.best-list')
bestitems = bestlists[0]
products = bestitems.select('ul > li')

# for 안에 for 넣는거 주의하기
# 크롤링한 데이터를 한번 더 크롤링해서 저장한다
for item in products:
        # > 랑 빈칸이랑 상관없음
    product_name = item.select_one('a.itemname')
    product_price = item.select_one('div.s-price > strong')
    product_info = [product_name.get_text().strip(), product_price.get_text()]
    product_lists.append(product_info)

write_excel_template('gmarket.xlsx', '상품정보', product_lists)

#gBestWrap > div > div:nth-child(5) > div > ul
#gBestWrap > div > div:nth-child(5) > div > ul > li:nth-child(1) > a
#gBestWrap > div > div:nth-child(5) > div > ul > li:nth-child(1) > div.item_price > div.s-price > strong > span > span