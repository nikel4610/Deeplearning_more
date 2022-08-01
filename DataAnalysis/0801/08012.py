import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from  matplotlib import font_manager, rc

df = open('./seoul.csv', encoding = 'cp949')
data = csv.reader(df, delimiter=',')

# 맨 윗쪽의 행 날려버림
next(data)
# print(header)

# 서울이 가장 더웠던 날
# 1. 질문 다듬기(추상화 단계 조절 = 질문 구체화 시키기)
# 2. 문제 해결 방법 구상
# 3. 구현

# max_temp = -999 # 최고 기온 값을 저장할 변수
# min_temp = 999 # 최저 기온 값을 저장할 변수

# max_date = '' # 최고 기온이 가장 높았던 날짜를 저장할 변수
# min_date = '' # 최고 기온이 가장 낮았던 날짜를 저장할 변수

# for row in data :
#     if row[-1] == '' :
#         row[-1] = 0 # 빈 문자열 자리를 0으로 채움
#     row[-1] = float(row[-1])

#     if max_temp < row[-1] :
#         max_date = row[0]
#         max_temp = row[-1]
    
#     if min_temp > row[-1] :
#         min_date = row[0]
#         min_temp = row[-1]
    

# df.close()

# print('기상 관측 이래 서울의 최고 기온이 가장 높았던 날은',max_date+'로, ', max_temp, '도 였습니다.')
# print('기상 관측 이래 서울의 최고 기온이 가장 낮았던 날은',min_date+'로, ', min_temp, '도 였습니다.')

font_path="C://Windows//Fonts//malgun.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font)

# # 내 생일의 기온 변화를 그래프로 그리기
# result = []

# # 최고 기온값이 존재하면 리스트에 값 추가
# for row in data:
#     if row[-1] != '':
#         result.append(float(row[-1]))

# high = []
# low = []

# for row in data :
#     if row[-1] != '' and row[-2] != '' : # 최고 기온과 최저 기온 값이 존재한다면
#         date = row[0].split('-') # 날짜 값을 – 문자를 기준으로 구분하여 저장
#         if 1997 <= int(row[0].split('-')[0]) : # 년도 설정
#             if row[0].split('-')[1] == '04' and row[0].split('-')[2] == '11' : # 월 일 설정
#                 high.append(float(row[-1])) # 최고 기온 값
#                 low.append(float(row[-2])) # 최저 기온 값

# plt.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지
# plt.title('내 생일의 기온 변화 그래프') # 제목 설정
# plt.plot(high, 'hotpink', label = 'high') # high 리스트에 저장된 값을 hotpink 색으로 그리고 레이블을 표시
# plt.plot(low, 'skyblue', label = 'low') # low 리스트에 저장된 값을 skyblue 색으로 그리고 레이블을 표시
# plt.xlabel('날짜') # x축 레이블 설정
# plt.ylabel('온도(섭씨)') # y축 레이블 설정
# plt.legend() # 범례 표시
# plt.show() # 그래프 나타내기

