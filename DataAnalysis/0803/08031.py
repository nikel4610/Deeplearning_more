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

# f = open('./subwaytime.csv')
# data = csv.reader(f)
# next(data)
# next(data)

# # 밤 11시에 사람들이 가장 많이 타고 내리는 역 찾기
# mx = 0
# mx_station = ''
# t = int(input('시간을 입력하세요: '))

# for row in data:
#     row[4: ] = map(int, row[4: ])
#     # 입력받은 승차 인원 값 추출
#     a = row[4 + (t - 4) * 2]
#     # 모든 데이터 탐색
#     if a > mx:
#         mx = a
#         mx_station = row[3] + '(' + row[1] + ')'

# print(mx_station, mx)

# # 시간대별 최대 승차 역 이름 및 승차 인원수 출력
# # 24개의 리스트 생성
# mx = [0] * 24
# mx_station = [''] * 24

# for row in data:
#     row[4: ] = map(int, row[4: ])
#     for j in range(24):
#         a = row[j * 2 + 4]
#         if a > mx[j]:
#             mx[j] = a 
#             mx_station[j] = row[3]

# print(mx_station)
# print(mx)

# plt.bar(range(24), mx)
# plt.xticks(range(24), mx_station, rotation = 90)
# plt.show()

# # 시간대별 승하차 인원 그래프 표현
# s_in = [0] * 24
# s_out = [0] * 24

# for row in data:
#     row[4: ] = map(int, row[4: ])
#     for i in range(24):
#         s_in[i] += row[i * 2 + 4] 
#         s_out[i] += row[i * 2 + 5]

# plt.style.use('ggplot')
# plt.plot(range(24), s_in, 'r', label = '승차')
# plt.plot(range(24), s_out, 'b', label = '하차')
# plt.legend()
# plt.show()

f = open('./age.csv') # cp949 error
data = csv.reader(f)
next(data)
data = list(data)

# 인구 구조가 비슷한 지역의 이름 찾기
name = input('지역의 이름을 입력하세요: ')
mn = 1
result_name = ''
result = 0

# 궁금한 지역의 인구 구조 저장
for row in data:
    if name in row[0]:
        home = np.array(row[3: ], dtype = int) / int(row[2]) 

# 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역 찾기
for row in data:
    away = np.array(row[3: ], dtype = int) / int(row[2]) 
    s = np.sum((home - away) ** 2)
    if s < mn and name not in row[0]:
        mn = s
        result_name = row[0]
        result = away

# 시각화
plt.style.use('ggplot')
plt.figure(figsize = (10, 5), dpi = 100)
plt.title(name +'의 인구 구조')
plt.plot(home, label = name)
plt.plot(result, label = result_name)
plt.legend()
plt.show()