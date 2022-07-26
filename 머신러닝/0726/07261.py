import numpy as np
import pandas as pd

# df.iloc[행 순서 번호, 열 순서 번호]
# df.iloc[0]: 전체 데이터프레임에서 0번쨰 행에 있는 값들만 출력
# df.loc[행 인덱스, 열 인덱스]
# df.loc[0]: 전체 데이터프레임에서 인덱스 이름이 0인 행만 출력

# df = pd.DataFrame(np.arange(10, 22).reshape(3, 4), index = ['a', 'b', 'c'], columns = ['A', 'B', 'C', 'D'])
# print(df)
# print(df.iloc[0]) # 행 순서 번호
# print(df.loc['a']) # 행 인덱스

# # df에서 17 데이터 값을 출력
# print(df.iloc[1, 3])
# print(df.loc['b', 'D'])

# # df에서 A열에서 값이 15이상인 데이터 추출
# print(df.A[df.A >= 15])

# # df에서 첫번째와 두번째 행을 추출
# print(df.iloc[[0, 1]])
# print(df.loc[['a', 'b']])
# # print(df.loc[0:2]) # error

# DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/lol.csv'
# df = pd.read_csv(DataUrl, sep='\t')

# # df의 마지막 행 데이터 출력
# print(df.iloc[-1]) # Series
# print(df.tail(1)) # DataFrame

# count(): 전체 데이터 개수 반환, NaN은 제외
# value_count(): 각각의 데이터 값의 개수를 반환, NaN은 제외
# s = pd.Series(range(10))
# s[5] = np.nan
# s[3] = np.nan
# print(s)
# print(s.count())
# print(s.value_counts())

# s2 = pd.Series(np.random.randint(6, size = 100))
# print(s2.value_counts())

# # sort_index(): 인덱스 정렬
# # sort_values(): 데이터 값 정렬
# print(s2.value_counts().sort_index())
# print(s2.value_counts().sort_values())

# print(s.sort_values()) # 오름차순 정렬(NaN은 마지막에 추가)
# print(s2.sort_values(ascending = False)) # 내림차순 정렬(default = 오름차순)

# s3 = pd.DataFrame(np.random.randint(6, size = (5, 5)))
# print(s3)
# print(s3.sort_values(by = 1)) # 인덱스 1열을 기준으로 정렬
# print(s3.sort_values(by = [1, 2])) # 인덱스 1열과 2열을 기준으로 정렬

# DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/Jeju.csv'
# df = pd.read_csv(DataUrl, encoding='euc-kr')

# # 컬럼타입이 수치형(정수, 실수)인 컬럼들의 이름(열 인덱스)을 출력
# print(df.select_dtypes(include=['int64', 'float64']).columns)
# # exclude는 DataFrame으로 반환

# # 컬럼타입이 범주형(문자형)인 컬럼들의 이름(열 인덱스)을 출력
# print(df.select_dtypes(include=['object']).columns)

# # 데이터프레임의 구조 출력
# print(df.info())

# # 컬럼타입이 수치형(정수, 실수)인 컬럼들의 사분위, 평균, 표준편차, 최대, 최소 출력
# print(df.describe())

# # '거주인구' 컬럼 값 출력
# print(df.loc[:, '거주인구'])

# # '평균 속도' 컬럼의 4분위 범위(IQR) 값을 출력
# print(df.loc[:, '평균 속도'].quantile(0.75) - df.loc[:, '평균 속도'].quantile(0.25))

# # '읍면동명' 컬럼의 유일값의 개수를 출력
# print(df.loc[:, '읍면동명'].nunique())

# # '읍면동명' 컬럼의 유일값 출력
# print(df.loc[:, '읍면동명'].unique())

DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/chipo.csv'
df = pd.read_csv(DataUrl)

# 'quantity' 컬럼 값이 3인 데이터를 추출해서 첫 5개의 행만 출력
print(df.loc[df['quantity'] == 3].head(5))

# 'quantity' 컬럼 값이 3인 데이터를 추출해서 행 index를 0부터 시작되도록 초기화 하고 첫 5개의 행만 출력
print(df.loc[df['quantity'] == 3].reset_index().head(5))

# item_price 컬럼의 달러 표시를 제거하고 float 타입으로 변환해서 new_price 컬럼으로 추가
df['new_price'] = df['item_price'].str.replace('$', '').astype(float)
print(df.head())

# new_price 컬럼의 5 이하의 값을 가지는 데이터프레임을 추출하고, 전체 개수 출력
print(len(df.loc[df['new_price'] <= 5]), '개')

# new_price 값이 9 이하이고 item_name 값이 Chicken Salad Bowl인 데이터 프레임 추출
print(df.loc[(df['new_price'] <= 9) & (df['item_name'] == 'Chicken Salad Bowl')])

# df의 new_price 컬럼 값에 따라 오름차순으로 정리하고 행 index를 초기화
df.sort_values(by='new_price', ascending=True).reset_index(drop = True)
print(df)

# df의 item_name 컬럼 값중 Chips를 포함하는 경우의 데이터를 출력
print(df.loc[df['item_name'].str.contains('Chips')])

# df의 짝수번째 컬럼만을 포함하는 데이터프레임 출력
print(df.iloc[::2])

# df의 new_price 컬럼 값에 따라 내림차순으로 정리하고 index 초기화
df.sort_values(by='new_price', ascending=False).reset_index(drop = True)
print(df)

# df의 item_name 컬럼 값이 Steak Salad 또는 Bowl인 데이터의 index 초기화
df.loc[(df['item_name'] == 'Steak Salad') | (df['item_name'] == 'Bowl')].reset_index(drop = True)

# df의 item_name 컬럼 값이 Steak Salad 또는 Bowl인 데이터를 데이터프레임화 한 후, item_name 기준으로 중복행 제거하되, 
# 첫번째 케이스는 남겨둠
df.loc[(df['item_name'] == 'Steak Salad') | (df['item_name'] == 'Bowl')].drop_duplicates(subset='item_name', keep='first')
print(df)
# 마지막 케이스는 keep = 'last'

# df의 데이터 중 item_name의 값이 Izze 데이터를 Fizzy lizzy로 변경
df.loc[df['item_name'] == 'Izze', 'item_name'] = 'Fizzy lizzy'
print(df)

# df의 데이터 중 new_price 값이 평균값 이상인 데이터를 추출하고 index 초기화
df.loc[df['new_price'] > df['new_price'].mean()].reset_index(drop = True)
print(df)