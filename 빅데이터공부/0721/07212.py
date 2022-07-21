import openpyxl

excel_file = openpyxl.load_workbook('tmp.xlsx')
print(excel_file.sheetnames)

excel_sheet = excel_file['상품정보']
for item in excel_sheet.rows:
    print(item[0].value, item[1].value)

excel_file.close()
