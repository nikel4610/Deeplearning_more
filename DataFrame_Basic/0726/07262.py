import numpy as np
import pandas as pd

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

# df의 데이터 중 choice_description 값에 Black이 들어가는 경우를 index를 초기화
df.loc[df['choice_description'].str.contains('Black', na = False)].reset_index(drop = True)
print(df)

# df의 데이터 중 choice_description 값이 NaN인 데이터의 개수를 구하고 출력
print(len(df.loc[pd.isnull(df['choice_description'])]))

# df의 데이터 중 choice_description 값이 NaN인 데이터를 loc를 사용하여 NoData로 대체
df.loc[pd.isnull(df['choice_description']), 'choice_description'] = 'NoData'
print(df)

# df의 데이터 중 choice_description 컬럼의 데이터값에 Vegetables가 들어가지 않는 데이터 개수 출력
print(len(df.loc[~df['choice_description'].str.contains('Vegetables')]))

# df의 데이터 중 item_name 컬럼값이 N으로 시작하는 데이터 출력
print(df.loc[df['item_name'].str.startswith('N')])

# df의 데이터 중 item_name 컬럼값의 문자 개수가 15개 이상인 데이터 출력
print(df.loc[df['item_name'].str.len() >= 15])

# df의 데이터 중 new_price값이 first 목록에 해당하는 경우 데이터 개수 출력
first = [1.69, 2.39, 3.39, 4.45, 9.25, 10.98, 11.75, 16.98]
print(len(df.loc[df['new_price'].isin(first)]))