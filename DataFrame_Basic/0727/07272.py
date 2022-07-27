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

# df = pd.read_csv('./tesla_stock_quandle.csv', parse_dates = [0])

# # 2016년 6월 데이터만 추출
# # print(df.loc[(df.Date.dt.year == 2016) & (df.Date.dt.month == 6)])
# # df.index = df['Date']
# # print(df.index)

# # print(df['2017-08'].iloc[:, :5])

# # 주식 데이터의 최초 수집 이후 경과된 시간 출력
# # print(df.index.max() - df.index.min()) # 242 days 00:00:00

# df['ref_date'] = df['Date'] - df['Date'].min()
# df.index = df['ref_date']
# print(df.iloc[:5, :5])

# # 주식 데이터의 수집 이후 최초의 5일 데이터 추출
# print(df['5day' :].iloc[:5, :5])

# 특정일에 누락된 데이터도 포함시켜 데이터를 살펴보려면 임의의 시간 범위를 생성하여 인덱스로 지정해야 함
# DatetimeIndex 라는 자료형으로 만들어진다
# DatetimeIndex 자료형에는 freq라는 속성이 있으며 freq 속성을 이용하여 시간 간격을 조절하여 인덱스 생성 가능
# freq 시간 주기
# B: business day, D: day, W: week, M: month, Q: quarter, A: year
# SM: semi-month, BM: business month, BQ: business quarter, BA: business year

# print(pd.date_range('2022-07-01', '2022-07-15', freq = 'B')) # 평일만 생성

# ts1 = pd.Series(np.random.randn(1000), index = pd.date_range('1/1/2019', periods = 1000))
# print(ts1.head(5))
# print(ts1.info())
# print(ts1['2021'].count())
# print(ts1['2021-07' : '2021-09'])

# dates = pd.date_range('1/1/2022', periods = 100, freq = 'W-WED')
# print(dates)

# print(pd.date_range(start = '2022-07-01', periods = 20))
# print(pd.date_range(end = '2022-07-01', periods = 20))

# print(pd.date_range('2022-01-01', '2022-07-01', freq = 'BM'))

# print(pd.date_range('2022-07-27', periods = 10, freq = '1h30min'))

# shift(): 데이터를 시간 축으로 앞이나 뒤로 이동
# dates = pd.Series(np.random.randn(4), index = pd.date_range('2022/01/01', periods = 4, freq = 'M'))
# print(dates)
# print(dates.shift(2))
# print(dates.shift(-2))
# print(dates.shift(2, freq = 'M'))

# resample(): 시간 간격을 재조정, (시간 구간을 작게 설정하면 데이터 양이 증가하므로 up-sampling, 시간 구간을 작게 설정하면
#                                 데이터 양이 감소하므로 down-sampling 이라고 부른다)
# dates = pd.Series(np.random.randn(100), index = pd.date_range('2022/01/01', periods = 100, freq = 'D'))
# print(dates.resample('W').mean())
# print(dates.resample('M').first())

# resampling 할 때 존재하지 않는 데이터를 ffill(), bfill() 사용하여 채워넣을 수 있다
# time_index = pd.date_range('1/1/2022', periods = 5, freq = 'M')
# df = pd.DataFrame(index = time_index)
# df['Sales'] = [100.0, 200.0, np.nan, np.nan, 500.0]
# print(df)
# print(df.interpolate()) # 연속된 데이터를 채워넣는다
# print(df.ffill()) # 누락된 값을 앞의 값으로 채워넣음
# print(df.bfill()) # 누락된 값을 뒤의 값으로 채워넣음

# print(df.interpolate(method = 'quadratic')) # 제곱근에 따라 연속된 데이터를 채워넣는다(비선형)
# print(df.interpolate(limit = 1, limit_direction = 'forward')) # 데이터 개수와 방향 지정

# # 주가 데이터
# df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/timeTest.csv')

# # Yr_Mo_Dy열을 datetime64타입으로 변환하고, 년도의 유일값을 모두 출력
# df['Yr_Mo_Dy'] = pd.to_datetime(df['Yr_Mo_Dy'])
# print(df['Yr_Mo_Dy'].dt.year.unique())

# # Yr_Mo_Dy열의 데이터 년도가 2061년 이상인 경우에는 모두 100을 뺀 날짜를 Yr_Mo_Dy열에 저장
# def fix_century(x):
#     if x.year > 2060:
#         return x.replace(year = x.year - 100)
#     else:
#         return x

# df['Yr_Mo_Dy'] = df['Yr_Mo_Dy'].apply(fix_century)
# print(df['Yr_Mo_Dy'].dt.year.unique())

# # 년도별 각 컬럼의 평균값 구하기
# print(df.groupby(df['Yr_Mo_Dy'].dt.year).mean())

# # Yr_Mo_Dy열의 날짜 데이터 요일을 추출하여 weekday 컬럼으로 추가
# df['weekday'] = df['Yr_Mo_Dy'].dt.weekday
# print(df.head(5))

# # weekday컬럼을 기준으로 주말이면 1, 평일이면 0의 값을 가지는 WeekCheck 컬럼을 만드시오
# df['WeekCheck'] = df['weekday'].apply(lambda x: 1 if x in [5, 6] else 0)
# print(df.head(5)) # weekday -> 월요일 0, 토요일 5, 일요일 6

# # Yr_Mo_Dy열을 기준으로 각월별 모든 컬럼의 평균을 출력하시오 (년도, 일자 상관없이)
# print(df.groupby(df['Yr_Mo_Dy'].dt.month).mean())

# # 모든 결측치는 컬럼 기준 직전의 값으로 대체하고 첫번째 행에 결측치가 있는 경우에는 뒤에 있는 값으로 대체하시오
# df = df.fillna(method = 'ffill').fillna(method = 'bfill')
# print(df.isnull().sum())

# # Yr_Mo_Dy열의 년도-월 기준으로 모든 컬럼의 평균값을 구하시오
# print(df.groupby(df['Yr_Mo_Dy'].dt.to_period('M')).mean())

# # RPT 컬럼의 값을 일자별 기준으로 1차차분하여 출력하시오
# df['diff'] = df['RPT'].diff()
# print(df.head(5))
# # diff(periods = 1, axis = 0) 은 행과 행의 차이 또는 열과 열의 차이 반환
# # axis = 0이면 행끼리 비교, axis = 1이면 열끼리 비교
# # periods는 비교할 간격을 지정, 기본값 1은 바로 이전값과 비교

# # RPT와 VAL 컬럼을 일주일 간격으로 각각 이동평균한 값을 구하시오
# print(df[['RPT', 'VAL']].rolling(window = 7).mean())
# # rolling(window, min_period = , win_type = , on = , axis = , method = ) : 이동 평균 함수

#서울시 미세먼지 데이터
df =pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/seoul_pm.csv')

# '(년-월-일:시)'컬럼을 datetime 자료형으로 변환하고 시는  24:00:00 형식으로  변경하시오


# '(년-월-일:시)'컬럼 데이터의 일자별 영어요일 이름을 'DayName'컬럼으로 추가하시오


# 'DayName'컬럼에 따른 'PM10등급'컬럼의 빈도수를 출력하시오 (pivot테이블로 생성)

# 시간이 연속 데이터로 존재하는지 (결측치가 없는지) 확인하시오


# 오전 10시와 오후 10시(22시)의 'PM10등급'컬럼의 평균값을 출력하시오


# '(년-월-일:시)'컬럼을 인덱스로 설정하시오


# 데이터를 주 단위로 뽑아서 최소, 최대, 평균, 표준편차를 출력하시오
