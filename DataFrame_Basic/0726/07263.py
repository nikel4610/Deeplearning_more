import numpy as np
import pandas as pd
import seaborn as sns

# DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/AB_NYC_2019.csv'
# df = pd.read_csv(DataUrl)

# # df 데이터의 각 host_name의 빈도수를 구하고 host_name으로 정렬하여 상위 5개 출력
# print(df['host_name'].value_counts().sort_index().head(5))
# print('############################################################')

# # df 데이터의 각 host_name의 빈도수를 구하고 빈도수 기준으로 내림차순 정렬한 데이터 프레임을 생성하고
# # 빈도수 컬럼은 'counts'로 변경
# df_counts = df['host_name'].value_counts().sort_values(ascending = False).to_frame()
# df_counts.columns = ['counts']
# print(df_counts.head(5))
# print('############################################################')

# # df의 데이터를 neighbourhood_group 컬럼 값으로 그룹화하고 neighbourhood 컬럼 값의 개수 출력
# print(df.groupby(['neighbourhood_group', 'neighbourhood'], as_index = False).size())
# print('############################################################')

# # df의 데이터를 neighbourhood_group 컬럼 값으로 그룹화에 따른 neighbourhood 컬럼 값의 최댓값 출력
# print(df.groupby(['neighbourhood_group', 'neighbourhood'], as_index = False).size().groupby(['neighbourhood_group'], as_index = False).max())
# print('############################################################')

# # df의 데이터를 neighbourhood_group 컬럼 값으로 그룹화에 따른 price컬럼값의 평균, 분산, 최대, 최소값 출력
# print(df.groupby(['neighbourhood_group', 'price'], as_index = False).agg({'price': ['mean', 'var', 'max', 'min']}))
# print('############################################################')

# df = pd.DataFrame({'A' : [1, 3, 4, 3, 4], 
#                    'B' : [2, 3, 1, 2, 3], 
#                    'C' : [1, 5, 2, 3, 4]})

# # df의 각 행의 데이터 최대값으로부터 최소값의 차를 출력
# print(df.max() - df.min())

# # df의 각 열의 데이터 최대값으로부터 최소값의 차를 출력
# print(df.max(axis = 1) - df.min(axis = 1))

# # apply(함수): 인수로 전달된 함수는 행 또는 열 데이터를 전달받아 함수 정의 동작 수행 후 반환
# # df의 각 행의 데이터 최대값으로부터 최소값의 차를 출력
# print(df.apply(lambda x: x.max() - x.min()))

# # df의 각 열의 데이터 최대값으로부터 최소값의 차를 출력
# print(df.apply(lambda x: x.max() - x.min(), axis = 1))

# titanic = sns.load_dataset('titanic')

# # age컬럼값 20을 기준으로 'adult'와 'child'로 구벼하는 범주 데이터를 새 컬럼(Adult)으로 titanic에 추가
# titanic['Adult'] = titanic['age'].apply(lambda x: 'adult' if x >= 20 else 'child')
# print(titanic)

# # titanic 데이터로부터 성별 인원수, 선실별 인원수, 사망/생존별 인원수 출력
# print(titanic['sex'].value_counts())
# print(titanic['pclass'].value_counts().sort_index())
# print(titanic['alive'].sort_values().value_counts())

# # titanic 데이터로 부터 승객의 평균 나이 출력
# print(titanic['age'].mean())

# # titanic 데이터로 부터 여성 승객의 평균 나이 출력
# print(titanic.loc[titanic.sex == 'female', 'age'].mean())

# # fillna(): 데이터값이 NaN을 원하는 값으로 변경
# # reset_index(): 기존의 행 인덱스를 열로 추가하고, 정수 기반의 행 인덱스를 새로 지정
# # set_index(): 기존의 행 인덱스를 삭제하고 데이터 열 중에 하나를 행 인덱스로 지정

# # cut(): 실수 값을 크기 기준으로 카테고리 갓으로 변환, bins인수에는 실수값의 경계선 목록을 지정
# #        labels 인수는 카테고리로 분류된 값의 범주이름을 지정
# ages = [0, 5, 10, 20, 25, 30, 35, 23, 33, 50, 53, 60, 80, 100, 105] # 연속 수치값 또는 정수값
# bins = [0, 18, 30, 50, 70, 100]
# labels = ['미성년', '청년', '중년', '장년', '노년'] # 범주 데이터값
# categories = pd.cut(ages, bins, labels = labels)
# print(categories)
# print(type(categories))

# stack(): 열 인덱스를 행 인덱스로 변환
# unstack(): 행 인덱스를 열 인덱스로 변환

# np.random.seed(0)
# df = pd.DataFrame(np.round(np.random.randn(6, 4), 2), columns = [["A", "A", "B", "B"], ["x1", "x2", "x1", "x2"]], 
#                             index = [["M", "M", "M", "F", "F", "F"], ["id1", "id2", "id3", "id1", "id2", "id3"]])
# print(df)

# df.columns.names = ["ColIdx1", "ColIdx2"]
# df.index.names = ["RowIdx1", "RowIdx2"]
# print(df)

# result = df.stack("ColIdx1")
# print(result)

# result2 = df.stack(1)
# print(result2)

# result3 = df.unstack("RowIdx2")
# print(result3)

# result4 = df.unstack(0)
# print(result4)

# # 그룹핑한 두개의 컬럼이 행인덱스가 되어 계층 구조로 출력됨
# print(df.groupby(['neighbourhood_group', 'neighbourhood']).price.mean())

# # 'neighbourhood_group', 'neighbourhood'로 그룹핑한 price컬럼값의 평균을 계측적으로 indexing없이 결과가 반환되도록 함
# print(df.groupby(['neighbourhood_group', 'neighbourhood']).price.mean().unstack())
# print(df.groupby(['neighbourhood', 'neighbourhood_group']).price.mean().unstack())

DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/BankChurnersUp.csv'
df = pd.read_csv(DataUrl, index_col = 0)

# df의 Income_Category 컬럼값을 다음 카테고리 범주 데이터로 변경하여 newIncome 컬럼으로 df에 추가
# 'Unknown': N
# 'Less than 40K': a
# '40K - 60K' = b
# '60K - 80K': c
# '80K - 120K': d
# '120K + ': e

df.apply(lambda x: x.astype(str).str.lower())
df['Income_Category'] = df['Income_Category'].apply(lambda x: x.lower())
df['newIncome'] = df['Income_Category'].apply(lambda x: 'a' if x == 'less than $40k' else 'b' if x == '$40k - $60k' else 
                                                'c' if x == '$60k - $80k' else 'd' if x == '$80k - $120k' else 'e' if x == '$120k +' else 'N')
print(df)

# Customer_Age 컬럼값의 나이 구간을 (0 ~ 9 : 0, 10 ~ 19 : 10 ...)로 변경하고 각 구간의 빈도수 출력
df['Customer_Age'] = df['Customer_Age'].apply(lambda x: x//10 * 10)
print(df['Customer_Age'].value_counts().sort_index())

# Education_Level 컬럼값 중 Graduate 단어가 포함되는 값은 1, 그렇지 않은 경우에는 0으로 변경하여 newEduLevel 컬럼으로 정의하고 빈도수 출력
df['Education_Level'] = df['Education_Level'].apply(lambda x: 1 if 'Graduate' in x else 0)
print(df['Education_Level'].value_counts())