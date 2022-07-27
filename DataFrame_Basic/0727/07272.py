import numpy as np
import pandas as pd

# 시계열 데이터 처리
# 주가 데이터
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/timeTest.csv')

from datetime import datetime
# 현재 날짜, 시간
print(datetime.now())
# 년 월 일 시 분 초
print(datetime(1971, 1, 1, 12, 35, 55))
