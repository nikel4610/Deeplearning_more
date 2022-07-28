import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as pdr
import datetime
import random

# #서울시 미세먼지 데이터
# df =pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/seoul_pm.csv')

# # '(년-월-일:시)'컬럼을 datetime 자료형으로 변환하고 시는  24:00:00 형식으로  변경하시오
# def change(x):
#     date = x.split(':')[0]
#     hour = x.split(':')[1]
#     if hour == '24':
#         hour = '00:00:00'
#         finaldate = pd.to_datetime(date + ' ' + hour) + datetime.timedelta(days=1)
#     else:
#         hour = hour + ':00:00'
#         finaldate = pd.to_datetime(date + ' ' + hour)
#     return finaldate

# df['(년-월-일:시)'] = df['(년-월-일:시)'].apply(change)
# print(df.head(5))

# # '(년-월-일:시)'컬럼 데이터의 일자별 영어요일 이름을 'DayName'컬럼으로 추가하시오
# df['DayName'] = df['(년-월-일:시)'].dt.day_name()
# print(df.head(5))

# # 'DayName'컬럼에 따른 'PM10등급'컬럼의 빈도수를 출력하시오 (pivot테이블로 생성)
# df_pivot = df.pivot_table(index='DayName', columns='PM10등급', values='PM10', aggfunc='count').fillna(0)
# print(df_pivot)

# # 시간이 연속 데이터로 존재하는지 (결측치가 없는지) 확인하시오
# # 시간을 차분한 경우 첫번째 데이터 값은 NaN, 두번째 데이터 값부턴는 동일한 값이 되므로 연속이라 판단 가능
# check = len(df['(년-월-일:시)'].diff().unique())
# print(check) # 2
# if check == 2:
#     print('시간이 연속 데이터로 존재합니다.')
# else:
#     print('시간이 연속 데이터가 아닙니다.')

# # 오전 10시와 오후 10시(22시)의 'PM10'컬럼의 평균값을 출력하시오
# print(df.groupby(df['(년-월-일:시)'].dt.hour).mean().iloc[[10,22],[0]])

# # '(년-월-일:시)'컬럼을 인덱스로 설정하시오
# df.set_index('(년-월-일:시)', inplace=True, drop = True)
# print(df.head(5))

# # 데이터를 주 단위로 뽑아서 최소, 최대, 평균, 표준편차를 출력하시오
# df.resample('w').agg(['min','max','mean','std'])

# # 코드 연습문제1
# # yesterday.txt파일을 읽어들여서 문장의 개수, 단어의 개수, yesterday(대소문자 구분하지 않음) 단어 개수를 출력
# text = open('./dataset/yesterday.txt', 'r', encoding='utf-8')
# sectences = text.readlines()
# print(type(sectences))
# print('문장 개수: ', len(sectences))

# word_count = 0
# for sectence in sectences:
#     word_count += len(sectence.split())
# print('단어 개수: ', word_count)

# count_yesterday = 0
# for sectence in sectences:
#     if 'yesterday' in sectence:
#         count_yesterday += 1
#     if 'Yesterday' in sectence:
#         count_yesterday += 1

# print('yesterday 단어 개수: ', count_yesterday)

# # 코드 연습문제2
# # 숫자를 입력받아 업 다운 게임을 한다. 기회는 다섯번.
# answer = random.randint(1, 101)

# for i in range(5):
#     a = int(input('숫자를 입력하세요 (1 ~ 100): '))
#     if a == answer:
#         print('정답입니다.')
#         break
#     elif a > answer:
#         print('입력한 숫자가 더 큽니다.')
#     else:
#         print('입력한 숫자가 더 작습니다.')
#     if i == 4:
#         print('실패하였습니다.')
#         print('정답은', answer, '입니다.')

