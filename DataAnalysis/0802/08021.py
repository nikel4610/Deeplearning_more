import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from  matplotlib import font_manager, rc
import matplotlib.colors as mcolors
import math

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

# f = open('gender.csv')
# data = csv.reader(f)

# m = []
# f = []

# # for row in data :
# #     if '신도림' in row[0] :
# #         for i in range(0,101) :
# #             m.append(int(row[i+3]))
# #             f.append(int(row[-(i+1)]))
# # f.reverse()

# for row in data :
#     if '무거' in row[0] :
#         for i in row[3:104] :
#             m.append(-int(i)) # 마이너스 부호를 넣어서 음수로 변경
#         for i in row[106:] :
#             f.append(int(i))

# plt.style.use('ggplot')
# # plt.figure(figsize = (10,5), dpi=300)
# plt.title('지역의 남녀 성별 인구 분포')
# plt.barh(range(101), m, label = '남성')
# plt.barh(range(101), f, label = '여성')
# plt.legend()
# plt.show()

# name = input()
# for row in data:
#     if name in row[0]:
#         for i in row[3:104]:
#             m.append(-int(i))
#         for i in row[106:]:
#             f.append(int(i))
#         break

# colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)

# # Sort colors by hue, saturation, value and name.
# by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgba(color)[:3])), name)
#                 for name, color in colors.items())
# sorted_names = [name for hsv, name in by_hsv]

# n = len(sorted_names)
# ncols = 4
# nrows = n // ncols

# fig, ax = plt.subplots(figsize=(9, 8), dpi = 300)

# # Get height and width
# X, Y = fig.get_dpi() * fig.get_size_inches()
# h = Y / (nrows + 1)
# w = X / ncols

# for i, name in enumerate(sorted_names):
#     row = i % nrows
#     col = i // nrows
#     y = Y - (row * h) - h

#     xi_line = w * (col + 0.05)
#     xf_line = w * (col + 0.25)
#     xi_text = w * (col + 0.3)

#     ax.text(xi_text, y, name, fontsize=(10),
#             horizontalalignment='left',
#             verticalalignment='center')

#     ax.hlines(y + h * 0.1, xi_line, xf_line,
#               color=colors[name], linewidth=(6))

# ax.set_xlim(0, X)
# ax.set_ylim(0, Y)
# ax.set_axis_off()

# fig.subplots_adjust(left=0, right=1,
#                     top=1, bottom=0,
#                     hspace=0, wspace=0)
# plt.show()

# plt.rc('font', family = 'Malgun Gothic')
# size = [2441, 2312, 1031, 1233]
# label = ['A형','B형','AB형', 'O형']
# color = ['darkmagenta', 'deeppink', 'hotpink', 'pink']
# plt.axis('equal')
# plt.pie(size, labels = label, autopct = '%.1f%%', explode = (0,0,0.1,0), colors = color)
# plt.legend()
# plt.show()

# size = []
# name = input('찾고 싶은 지역의 이름을 알려주세요 : ')
# for row in data :
#     if name in row[0] :
#         m = 0
#         f = 0
#         for i in range(101) :
#             m += int(row[i+3])
#             f += int(row[i+106])
#         break
# size.append(m)
# size.append(f)

# plt.rc('font', family ='Malgun Gothic')
# color = ['crimson', 'darkcyan']
# plt.axis('equal')
# plt.pie(size, labels = ['남','여'], autopct ='%.1f%%', colors = color, startangle =90)
# plt.title(name + ' 지역의 남녀 성별 비율')
# plt.show()

# size = []
# name = input('궁금한 동네를 입력해주세요 : ')
# for row in data :
#     if name in row[0] :
#         for i in range(3,104) :
#             m.append(int(row[i]))
#             f.append(int(row[i+103]))
#             size.append(math.sqrt(int(row[i]) + int(row[i+103])))
#         break

# plt.style.use('ggplot')
# plt.rc('font',family='Malgun Gothic')
# plt.figure(figsize = (10,5), dpi=300)
# plt.title(name+' 지역의 성별 인구 그래프')
# plt.scatter(m, f, s = size, c = range(101), alpha=0.5, cmap='jet')
# plt.colorbar()
# plt.plot(range(max(m)),range(max(m)), 'g')
# plt.xlabel('남성 인구 수')
# plt.ylabel('여성 인구 수')
# plt.show()

f = open('./subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)

# mx = 0
# rate = 0

# for row in data :
#     for i in range(4,8) :
#         row[i] = int(row[i])
#     if row[6] != 0 and (row[4] + row[6]) > 100000 :
#         rate = row[4] / (row[4] + row[6])
#         if rate > mx :
#             mx = rate
#             mx_station = row[3] + ' ' + row[1]

# print(mx_station, round(mx * 100,2))

# label = ['유임승차','유임하차','무임승차','무임하차']
# c = ['#14CCC0', '#389993', '#FF1C6A', '#CC14AF']
# plt.rc('font', family = 'Malgun Gothic')
# for row in data :
#     for i in range(4,8) :
#         row[i] = int(row[i])
# plt.figure(dpi = 300)
# plt.title(row[3] + ' ' + row[1])
# plt.pie(row[4:8], labels = label, colors = c, autopct = '%1.f%%')
# plt.axis('equal')
# plt.show()

# mx = [0] * 4
# mx_station = [''] * 4
# label = ['유임승차', '유임하차', '무임승차', '무임하차']
# for row in data:
#     for i in range(4, 8):
#         row[i] = int(row[i])
#         if row[i] > mx[i-4]:
#             mx[i-4] = row[i]
#             mx_station[i-4] = row[3] + ' ' + row[1]
# for i in range(4):
#     print(label[i] + ' : ' + mx_station[i], mx[i])

# result = []
# for row in data:
#     row[4: ] = map(int, row[4: ])
#     result.append(row[10])
# result.sort()

# 아침 7 ~ 9시 승차 인원 최대 역 과 인원수 찾기
mx = 0
mx_station = ''
for row in data:
    row[4: ] = map(int, row[4: ])
    if sum(row[10:15:2]) > mx:
        mx = sum(row[10:15:2])
        mx_station = row[3] + '(' + row[1] + ')'

print(mx_station, mx)
