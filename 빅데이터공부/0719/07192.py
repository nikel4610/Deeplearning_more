import pandas as pd
import numpy as np
from IPython.display import display 

titanic_df = pd.read_csv('titanic_train.csv')

# pd.set_option('display.max_colwidth', 200)
# titanic_df = pd.read_csv('titanic_train.csv')
# titanic_boolean = titanic_df[titanic_df['Age'] > 60]
# print(type(titanic_boolean))
# print(titanic_boolean)

# print(titanic_df[titanic_df['Age'] > 60][['Name','Age']].head(3))
# print(titanic_df.loc[titanic_df['Age'] > 60, ['Name','Age']].head(3))
# print(titanic_df[ (titanic_df['Age'] > 60) & (titanic_df['Pclass']==1) & (titanic_df['Sex']=='female')])

# cond1 = titanic_df['Age'] > 60
# cond2 = titanic_df['Pclass']==1
# cond3 = titanic_df['Sex']=='female'
# print(titanic_df[ cond1 & cond2 & cond3])

# # Aggregation 함수, Sort 정렬
# # 이름으로 정렬
# titanic_sorted = titanic_df.sort_values(by=['Name'])
# print(titanic_sorted.head(3))

# # Pclass와 Name으로 내림차순 정렬
# titanic_sorted = titanic_df.sort_values(by=['Pclass', 'Name'], ascending=False)
# print(titanic_sorted.head(3))

# print(titanic_df[['Age', 'Fare']].mean())
# print(titanic_df[['Age', 'Fare']].sum())
# print(titanic_df[['Age', 'Fare']].count())

# titanic_groupby = titanic_df.groupby(by='Pclass')
# print(type(titanic_groupby))

# print(titanic_groupby[['Age', 'Fare']])
# print(titanic_groupby[['Age', 'Fare']].count())

# titanic_groupby = titanic_df.groupby('Pclass').count()
# print(titanic_groupby)

# titanic_groupby = titanic_df.groupby('Pclass')[['PassengerId', 'Survived']].count()
# print(titanic_groupby)

# # titanic_df.groupby('Pclass')['Age'].max(), titanic_df.groupby('Pclass')['Age'].min()
# print(titanic_df.groupby('Pclass')['Age'].agg([max, min]))

# agg_format={'Age':'max', 'SibSp':'sum', 'Fare':'mean'}
# print(titanic_df.groupby('Pclass').agg(agg_format))

# # Age 중복값일 경우 마지막 값인 mean이 출력됨
# agg_format={'Age':'max', 'Age':'mean', 'Fare':'mean'}
# titanic_df.groupby('Pclass').agg(agg_format)

# # 밑의 방식으로 col을 새로 추가하면 따로 출력됨
# print(titanic_df.groupby(['Pclass']).agg(age_max=('Age', 'max'), age_mean=('Age', 'mean'), fare_mean=('Fare', 'mean')))

# # 위의 방법과 똑같은 방식
# # 위의 방법이 좀 더 간결해서 좋은거같다.
# print(
# titanic_df.groupby('Pclass').agg(
#  age_max=pd.NamedAgg(column='Age', aggfunc='max'),
#  age_mean=pd.NamedAgg(column='Age', aggfunc='mean'),
#  fare_mean=pd.NamedAgg(column='Fare', aggfunc='mean')
# )
# )

# 결손 데이터 처리 isna, fillna
# 데이터처리에서 NaN값 처리는 필수!
print(titanic_df.isna().head(3))
print(titanic_df.isna( ).sum( )) # 각 col 별 NaN 개수 출력

titanic_df['Cabin'] = titanic_df['Cabin'].fillna('C000') # NaN을 C000로 채움
print(titanic_df.head(3))

titanic_df['Age'] = titanic_df['Age'].fillna(titanic_df['Age'].mean())
titanic_df['Embarked'] = titanic_df['Embarked'].fillna('S')
print(titanic_df.isna().sum())

print(titanic_df['Name'].value_counts())

# nunique() : 유일한 값의 개수를 출력
print(titanic_df['Pclass'].nunique())
print(titanic_df['Survived'].nunique())
print(titanic_df['Name'].nunique())

# replace로 원본 값 대체
replace_test_df = pd.read_csv('titanic_train.csv')

# Sex의 male값을 Man
print(replace_test_df['Sex'].replace('male', 'Man'))

replace_test_df['Sex'] = replace_test_df['Sex'].replace({'male':'Man', 'female':'Woman'})
replace_test_df['Cabin'] = replace_test_df['Cabin'].replace(np.nan, 'C001')
print(replace_test_df['Cabin'].value_counts(dropna=False))

