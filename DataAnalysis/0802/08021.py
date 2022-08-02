import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from  matplotlib import font_manager, rc

font_path="C://Windows//Fonts//malgun.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font)
plt.rcParams['axes.unicode_minus'] = False

# df = open('./seoul.csv', encoding = 'cp949')
# df = open('./age.csv', encoding = 'cp949')
# data = csv.reader(df, delimiter=',')
# next(data)

# jan = []
# aug = []

# for row in data:
#     month = row[0].split('-')[1]
#     if row[-1] != '':
#         if month == '01':
#             jan.append(float(row[-1]))
#         if month == '08':
#             aug.append(float(row[-1]))

# plt.boxplot([aug, jan])
# plt.show()

# # 1월부터 12월까지 최고 기온 데이터를 상자 그림으로 표현하기
# month = ([], [], [], [], [], [], [], [], [], [], [], [])

# for row in data:
#     if row[-1] != '':
#         month[int(row[0].split('-')[1])-1].append(float(row[-1]))

# plt.boxplot(month)
# plt.show()

# # 4월 1일부터 4월 31일까지의 최고 기온 데이터를 상자 그림으로 표현하기
# # April = [[] for i in range(31)]
# April = ([], [], [], [], [], [], [], [], [], [],
#         [], [], [], [], [], [], [], [], [], [],
#         [], [], [], [], [], [], [], [], [], [], [])

# for row in data:
#     if row[-1] != '':
#         if int(row[0].split('-')[1]) == 4:
#             April[int(row[0].split('-')[2])-1].append(float(row[-1]))

# plt.boxplot(April)
# plt.show()

# df = open('./age.csv', encoding = 'utf-8') # -> error
# data = csv.reader(df, delimiter=',')

# result = []
# for row in data:
#     if '울산광역시' in row[0]: # <- '울산광역시' is the problem idk why
#         for i in row [3:]:
#             result.append(int(i))

# plt.style.use('ggplot')
# plt.plot(result)
# plt.show()

# f = open('./age.csv')
# data = csv.reader(f)

# result = []
# for row in data :
#     if '신도림' in row[0] :
#         for i in row[3:] :
#             result.append(int(i))

# plt.bar(range(101), result)
# plt.show()

f = open('gender.csv')
data = csv.reader(f)

m = []
f = []

# for row in data :
#     if '신도림' in row[0] :
#         for i in range(0,101) :
#             m.append(int(row[i+3]))
#             f.append(int(row[-(i+1)]))
# f.reverse()

for row in data :
    if '무거' in row[0] :
        for i in row[3:104] :
            m.append(-int(i)) # 마이너스 부호를 넣어서 음수로 변경
        for i in row[106:] :
            f.append(int(i))

plt.style.use('ggplot')
# plt.figure(figsize = (10,5), dpi=300)
plt.title('지역의 남녀 성별 인구 분포')
plt.barh(range(101), m, label = '남성')
plt.barh(range(101), f, label = '여성')
plt.legend()
plt.show()