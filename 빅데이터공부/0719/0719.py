import pandas as pd

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

# Index 객체
# Index 객체 추출
indexes = titanic_df.index
print(indexes)
# Index 객체를 실제 값 arrray로 변환
print('Index 객체 array값:\n',indexes.values)

# indexes[0] = 5 # error: 이미 5가 있음

print(type(indexes.values))
print(indexes.values.shape)
print(indexes[:5].values)
print(indexes.values[:5])
print(indexes[6])

print(titanic_df.head(3))
titanic_reset_df = titanic_df.reset_index(inplace=False)
print(titanic_reset_df.head(3))

titanic_df['Pclass'].value_counts()

print('### before reset_index ###')
value_counts = titanic_df['Pclass'].value_counts()
print(value_counts)
print('value_counts 객체 변수 타입과 shape:',type(value_counts), value_counts.shape)

new_value_counts_01 = value_counts.reset_index(inplace=False)
print('### After reset_index ###')
print(new_value_counts_01)
print('new_value_counts_01 객체 변수 타입과 shape:',type(new_value_counts_01), new_value_counts_01.shape)

new_value_counts_02 = value_counts.reset_index(drop=True, inplace=False)
print('### After reset_index with drop ###')
print(new_value_counts_02)
print('new_value_counts_02 객체 변수 타입과 shape:',type(new_value_counts_02), new_value_counts_02.shape)

print(titanic_df['Pclass'].value_counts().reset_index())

# DataFrame의 rename()은 인자로 columns를 dictionary 형태로 받으면 '기존 컬럼명':'신규 컬럼명' 형태로 변환
new_value_counts_01 = titanic_df['Pclass'].value_counts().reset_index()
print(new_value_counts_01.rename(columns={'index':'Pclass', 'Pclass':'Pclass_count'}))


