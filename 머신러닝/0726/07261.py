import numpy as np
import pandas as pd

# df.iloc[행 순서 번호, 열 순서 번호]
# df.iloc[0]: 전체 데이터프레임에서 0번쨰 행에 있는 값들만 출력
# df.loc[행 인덱스, 열 인덱스]
# df.loc[0]: 전체 데이터프레임에서 인덱스 이름이 0인 행만 출력

df = pd.DataFrame(np.arange(10, 22).reshape(3, 4), index = ['a', 'b', 'c'], columns = ['A', 'B', 'C', 'D'])
print(df)
print(df.iloc[0]) # 행 순서 번호
print(df.loc['a']) # 행 인덱스

# df에서 17 데이터 값을 출력
print(df.iloc[1, 3])
print(df.loc['b', 'D'])

# df에서 A열에서 값이 15이상인 데이터 추출
print(df.A[df.A >= 15])

# df에서 첫번째와 두번째 행을 추출
print(df.iloc[[0, 1]])
print(df.loc[['a', 'b']])
# print(df.loc[0:2]) # error

DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/lol.csv'
df = pd.read_csv(DataUrl, sep='\t')

# df의 마지막 행 데이터 출력
print(df.iloc[-1]) # Series
print(df.tail(1)) # DataFrame

# count(): 전체 데이터 개수 반환, NaN은 제외
# value_count(): 각각의 데이터 값의 개수를 반환, NaN은 제외
s = pd.Series(range(10))
s[5] = np.nan
s[3] = np.nan
print(s)
print(s.count())
print(s.value_counts())

s2 = pd.Series(np.random.randint(6, size = 100))
print(s2.value_counts())

# sort_index(): 인덱스 정렬
# sort_values(): 데이터 값 정렬
print(s2.value_counts().sort_index())
print(s2.value_counts().sort_values())

print(s.sort_values()) # 오름차순 정렬(NaN은 마지막에 추가)
print(s2.sort_values(ascending = False)) # 내림차순 정렬(default = 오름차순)

s3 = pd.DataFrame(np.random.randint(6, size = (5, 5)))
print(s3)
print(s3.sort_values(by = 1)) # 인덱스 1열을 기준으로 정렬
print(s3.sort_values(by = [1, 2])) # 인덱스 1열과 2열을 기준으로 정렬

DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/Jeju.csv'
df = pd.read_csv(DataUrl, encoding='euc-kr')

# 컬럼타입이 수치형(정수, 실수)인 컬럼들의 이름(열 인덱스)을 출력
print(df.select_dtypes(include=['int64', 'float64']).columns)
# exclude는 DataFrame으로 반환

# 컬럼타입이 범주형(문자형)인 컬럼들의 이름(열 인덱스)을 출력
print(df.select_dtypes(include=['object']).columns)

# 데이터프레임의 구조 출력
print(df.info())

# 컬럼타입이 수치형(정수, 실수)인 컬럼들의 사분위, 평균, 표준편차, 최대, 최소 출력
print(df.describe())

# '거주인구' 컬럼 값 출력
print(df.loc[:, '거주인구'])

# '평균 속도' 컬럼의 4분위 범위(IQR) 값을 출력
print(df.loc[:, '평균 속도'].quantile(0.75) - df.loc[:, '평균 속도'].quantile(0.25))

# '읍면동명' 컬럼의 유일값의 개수를 출력
print(df.loc[:, '읍면동명'].nunique())

# '읍면동명' 컬럼의 유일값 출력
print(df.loc[:, '읍면동명'].unique())