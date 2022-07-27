import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as pdr

#서울시 미세먼지 데이터
df =pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/seoul_pm.csv')

# '(년-월-일:시)'컬럼을 datetime 자료형으로 변환하고 시는  24:00:00 형식으로  변경하시오


# '(년-월-일:시)'컬럼 데이터의 일자별 영어요일 이름을 'DayName'컬럼으로 추가하시오


# 'DayName'컬럼에 따른 'PM10등급'컬럼의 빈도수를 출력하시오 (pivot테이블로 생성)

# 시간이 연속 데이터로 존재하는지 (결측치가 없는지) 확인하시오


# 오전 10시와 오후 10시(22시)의 'PM10등급'컬럼의 평균값을 출력하시오


# '(년-월-일:시)'컬럼을 인덱스로 설정하시오


# 데이터를 주 단위로 뽑아서 최소, 최대, 평균, 표준편차를 출력하시오