import csv
data_file = open('빅데이터공부/0722/USvideos.csv', 'r', encoding='utf-8-sig')
data_lines = csv.reader(data_file, delimiter=',')

for data_line in data_lines:
    print (data_line)
    break

data_file.close()