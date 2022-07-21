import openpyxl

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
    excel_sheet.column_dimensions['A'].width = 100
    excel_sheet.column_dimensions['B'].width = 20

    if sheetname != '':
        excel_sheet.title = sheetname

    # 한 줄 씩 집어넣는다
    for item in listdata:
        excel_sheet.append(item)
        
    excel_file.save(filename)
    excel_file.close()