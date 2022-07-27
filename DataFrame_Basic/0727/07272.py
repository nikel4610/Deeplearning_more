import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as pdr

# # 시계열 데이터 처리
# from datetime import datetime
# # # 현재 날짜, 시간
# # print(datetime.now())
# # # 년 월 일 시 분 초
# # print(datetime(1971, 1, 1, 12, 35, 55))

# # # datetime 객체는 시간계산이 용이하다
# # t1 = datetime(1971, 1, 1, 12, 35, 55)
# # t2 = datetime(1971, 12, 12)
# # print(t2 - t1)
# # print(type(t1), type(t2)) # datetime.datetime
# # print(type(t2 - t1)) # timedelta

# # 날짜 시간 형식의 문자열 데이터는 시간 계산을 위해 datetime으로 변환해야 한다
# # -> to_datetime()

# ebola = pd.read_csv('./dataset/country_timeseries.csv')
# ebola['date_dt'] = pd.to_datetime(ebola['Date'])

# # 날짜 시간 형식의 문자열 데이터를 datetime으로 변환할 때 원하는 형태로 변환 가능
# test_df1 = pd.DataFrame({'order_date':['01/01/20', '02/02/21', '03/01/22']})
# test_df1['dt1'] = pd.to_datetime(test_df1['order_date'], format='%d/%m/%y')

# # 시간 형식 문자
# # %a, %A: 요일
# # %w: 요일 숫자 (0은 일요일)
# # %b, %B: 월 이름
# # %y, %Y: 년도(2자리년도 , 4자리년도)
# # %H , %M, %S: 시(24시간), 분, 초
# # %I, %M, %S: 시(12시간), 분, 초
# # %p: 오전/오후
# # %z %Z: 시간대
# # %u: 요일 숫자 (1은 일요일)

# ebola1 = pd.read_csv('./dataset/country_timeseries.csv', parse_dates = ['Date'])
# print(ebola1.Date.dt.year)
# print(ebola1.Date.dt.month)
# print(ebola1.Date.dt.day)

# # 컬럼 데이터를 문자열로 처리하려면 str 접근자를 사용해서 문자열 메서드를 사용
# # 날짜 시간 컬럼 데이터를 datetime 유용하게 메서드를 사용하려면 dt접근자 사용

# ebola1['month'] = ebola1['Date'].dt.month
# ebola1['day'] = ebola1['Date'].dt.day
# print(ebola1.info())

# print(ebola1['Date'].min()) # 에볼라 바이러스가 발생을 기록한 최초 날짜
# print(type(ebola1['Date'].min())) # pandas의 Timestamp.Timestamp

# # 데이터의 모든 행에서 에볼라 바이러스 발생 기록된 최초의 날짜를 빼면 진행된 일 수 확인 가능
# ebola1['outbreak_days'] = ebola1['Date'].max() - ebola1['Date'].min() # 289days
# print(ebola1[['Date', 'Day' , 'outbreak_days']])

# df = pd.read_csv('./dataset/banklist.csv')

# # df로부터 데이터를 로드하여 dataframe을 생성하고 은행이 파산한 연도와 분기를 새로운 열로 추가하시오
# # 은행파산 날짜 저장열은 'Closing Date'
# df['Closing Date'] = pd.to_datetime(df['Closing Date'])
# df['year'] = df['Closing Date'].dt.year
# df['quarter'] = df['Closing Date'].dt.quarter
# print(df[['Bank Name', 'year', 'quarter']])

# # 연도별로 파산한 은행 개수 출력
# df_group = df.groupby('year')
# print(df_group.count()['Bank Name'])

# # 분기별로 파산한 은행 개수 출력
# df_group1 = df.groupby('quarter')
# print(df_group.count()['Bank Name'])

# # 년도별 파산한 은행 개수 변화를 선 그래프로 표현
# fig = plt.subplot()
# ax = plt.subplot()
# ax = df_group.count()['Bank Name'].plot(kind='line')
# plt.show()

# # 년도와 분기별 파산한 은행 개수 변화를 선 그래프로 표현
# fig2 = plt.subplot()
# ax2 = plt.subplot()
# ax2 = df_group1.count()['Bank Name'].plot(kind='line')
# plt.show()

# tesla = pdr.get_data_quandl('TSLA', api_key='')
# tesla.to_csv('./tesla_stock_quandle.csv')

df = pd.read_csv('./tesla_stock_quandle.csv')
# 날짜, 시작가, 종가, 최고가, 최저가, 거래수 ...
print(df.head())
print(df.info())