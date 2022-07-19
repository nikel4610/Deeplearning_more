import pandas as pd
from IPython.display import display 

titanic_df = pd.read_csv('titanic_train.csv')

# titanic_df['Age_0']=0
# titanic_df.head(3)

# titanic_df['Age_by_10'] = titanic_df['Age']*10
# titanic_df['Family_No'] = titanic_df['SibSp'] + titanic_df['Parch']+1
# titanic_df.head(3)

# titanic_df['Age_by_10'] = titanic_df['Age_by_10'] + 100
# titanic_df.head(3)

# # DataFrame 데이터 삭제
# titanic_drop_df = titanic_df.drop('Age_0', axis=1 )
# print(titanic_drop_df.head(3))
# print(titanic_df.head(3))

# pd.set_option('display.width', 1000)
# pd.set_option('display.max_colwidth', 15)
# print('#### before axis 0 drop ####')
# print(titanic_df.head(6))

# titanic_df.drop([0,1,2], axis=0, inplace=True)
# print('#### after axis 0 drop ####')
# print(titanic_df.head(3))

# # Index 객체
# # Index 객체 추출
# indexes = titanic_df.index
# print(indexes)
# # Index 객체를 실제 값 arrray로 변환
# print('Index 객체 array값:\n',indexes.values)

# # indexes[0] = 5 # error: 이미 5가 있음

# print(type(indexes.values))
# print(indexes.values.shape)
# print(indexes[:5].values)
# print(indexes.values[:5])
# print(indexes[6])

# print(titanic_df.head(3))
# titanic_reset_df = titanic_df.reset_index(inplace=False)
# print(titanic_reset_df.head(3))

# titanic_df['Pclass'].value_counts()

# print('### before reset_index ###')
# value_counts = titanic_df['Pclass'].value_counts()
# print(value_counts)
# print('value_counts 객체 변수 타입과 shape:',type(value_counts), value_counts.shape)

# new_value_counts_01 = value_counts.reset_index(inplace=False)
# print('### After reset_index ###')
# print(new_value_counts_01)
# print('new_value_counts_01 객체 변수 타입과 shape:',type(new_value_counts_01), new_value_counts_01.shape)

# new_value_counts_02 = value_counts.reset_index(drop=True, inplace=False)
# print('### After reset_index with drop ###')
# print(new_value_counts_02)
# print('new_value_counts_02 객체 변수 타입과 shape:',type(new_value_counts_02), new_value_counts_02.shape)

# print(titanic_df['Pclass'].value_counts().reset_index())

# # DataFrame의 rename()은 인자로 columns를 dictionary 형태로 받으면 '기존 컬럼명':'신규 컬럼명' 형태로 변환
# new_value_counts_01 = titanic_df['Pclass'].value_counts().reset_index()
# print(new_value_counts_01.rename(columns={'index':'Pclass', 'Pclass':'Pclass_count'}))

# DataFrame 인덱싱 및 필터링
# 거의 안씀

# DataFrame객체에서 []연산자내에 한개의 컬럼만 입력하면 Series 객체를 반환 
# series = titanic_df['Name']
# print(series.head(3))
# print("## type:",type(series), 'shape:', series.shape)

# # DataFrame객체에서 []연산자내에 여러개의 컬럼을 리스트로 입력하면 그 컬럼들로 구성된 DataFrame 반환 
# filtered_df = titanic_df[['Name', 'Age']]
# display(filtered_df.head(3))
# print("## type:", type(filtered_df), 'shape:', filtered_df.shape)

# # DataFrame객체에서 []연산자내에 한개의 컬럼을 리스트로 입력하면 한개의 컬럼으로 구성된 DataFrame 반환
# one_col_df = titanic_df[['Name']]
# display(one_col_df.head(3))
# print("## type:", type(one_col_df), 'shape:', one_col_df.shape)

# # print('[ ] 안에 숫자 index는 KeyError 오류 발생:\n', titanic_df[0]) # error

# #혼돈이 있을수 있으니, iloc loc 사용.
# print(titanic_df[0:2])
# print(titanic_df[ titanic_df['Pclass'] == 3].head(3))

# # DataFrame iloc[] 연산자
data = {'Name': ['Chulmin', 'Eunkyung','Jinwoong','Soobeom'],
 'Year': [2011, 2016, 2015, 2015],
 'Gender': ['Male', 'Female', 'Male', 'Male']
 }
data_df = pd.DataFrame(data, index=['one','two','three','four'])
# print(data_df)
# print(data_df.iloc[0, 0])

# # 아래 코드는 오류를 발생합니다. 
# # data_df.iloc[0, 'Name']

# # 아래 코드는 오류를 발생합니다. 
# # data_df.iloc['one', 0]


# print("\n iloc[1, 0] 두번째 행의 첫번째 열 값:", data_df.iloc[1,0])
# print("\n iloc[2, 1] 세번째 행의 두번째 열 값:", data_df.iloc[2,1])
# print("\n iloc[0:2, [0,1]] 첫번째에서 두번째 행의 첫번째, 두번째 열 값:\n", data_df.iloc[0:2, [0,1]])
# print("\n iloc[0:2, 0:3] 첫번째에서 두번째 행의 첫번째부터 세번째 열값:\n", data_df.iloc[0:2, 0:3])
# print("\n 모든 데이터 [:] \n", data_df.iloc[:])
# print("\n 모든 데이터 [:, :] \n", data_df.iloc[:, :])
# print("\n 맨 마지막 칼럼 데이터 [:, -1] \n", data_df.iloc[:, -1])
# print("\n 맨 마지막 칼럼을 제외한 모든 데이터 [:, :-1] \n", data_df.iloc[:, :-1])

# # iloc[]는 불린 인덱싱을 지원하지 않아서 아래는 오류를 발생.
# # print("\n ix[data_df.Year >= 2014] \n", data_df.iloc[data_df.Year >= 2014])

data_df.loc['one', 'Name']

# 다음 코드는 오류를 발생합니다. 
# data_df.loc[0, 'Name']

print('위치기반 iloc slicing\n', data_df.iloc[0:1, 0],'\n')
print('명칭기반 loc slicing\n', data_df.loc['one':'two', 'Name'])

print('인덱스 값 three인 행의 Name칼럼값:', data_df.loc['three', 'Name'])
print('\n인덱스 값 one 부터 two까지 행의 Name과 Year 칼럼값:\n', data_df.loc['one':'two', ['Name', 'Year']])
print('\n인덱스 값 one 부터 three까지 행의 Name부터 Gender까지의 칼럼값:\n', data_df.loc['one':'three', 'Name':'Gender'])
print('\n모든 데이터 값:\n', data_df.loc[:])
print('\n불린 인덱싱:\n', data_df.loc[data_df.Year >= 2014])
