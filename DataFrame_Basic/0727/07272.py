import numpy as np
import pandas as pd

# 시계열 데이터 처리
# 주가 데이터
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/timeTest.csv')

from datetime import datetime
# # 현재 날짜, 시간
# print(datetime.now())
# # 년 월 일 시 분 초
# print(datetime(1971, 1, 1, 12, 35, 55))

# # datetime 객체는 시간계산이 용이하다
# t1 = datetime(1971, 1, 1, 12, 35, 55)
# t2 = datetime(1971, 12, 12)
# print(t2 - t1)
# print(type(t1), type(t2)) # datetime.datetime
# print(type(t2 - t1)) # timedelta

# 날짜 시간 형식의 문자열 데이터는 시간 계산을 위해 datetime으로 변환해야 한다
# -> to_datetime()


