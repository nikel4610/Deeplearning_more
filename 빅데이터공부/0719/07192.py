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

# # 결손 데이터 처리 isna, fillna
# # 데이터처리에서 NaN값 처리는 필수!
# print(titanic_df.isna().head(3))
# print(titanic_df.isna( ).sum( )) # 각 col 별 NaN 개수 출력

# titanic_df['Cabin'] = titanic_df['Cabin'].fillna('C000') # NaN을 C000로 채움
# print(titanic_df.head(3))

# titanic_df['Age'] = titanic_df['Age'].fillna(titanic_df['Age'].mean())
# titanic_df['Embarked'] = titanic_df['Embarked'].fillna('S')
# print(titanic_df.isna().sum())

# print(titanic_df['Name'].value_counts())

# # nunique() : 유일한 값의 개수를 출력
# print(titanic_df['Pclass'].nunique())
# print(titanic_df['Survived'].nunique())
# print(titanic_df['Name'].nunique())

# # replace로 원본 값 대체
# replace_test_df = pd.read_csv('titanic_train.csv')

# # Sex의 male값을 Man
# print(replace_test_df['Sex'].replace('male', 'Man'))

# replace_test_df['Sex'] = replace_test_df['Sex'].replace({'male':'Man', 'female':'Woman'})
# replace_test_df['Cabin'] = replace_test_df['Cabin'].replace(np.nan, 'C001')
# print(replace_test_df['Cabin'].value_counts(dropna=False))

# apply lambda 식으로 데이터 가공
def get_square(a):
    return a**2
print('3의 제곱은:',get_square(3))

lambda_square = lambda x : x ** 2
print('3의 제곱은:',lambda_square(3))

a=[1,2,3]
squares = map(lambda x : x**2, a)
print(list(squares))

titanic_df['Name_len']= titanic_df['Name'].apply(lambda x : len(x))
print(titanic_df[['Name','Name_len']].head(3))

titanic_df['Child_Adult'] = titanic_df['Age'].apply(lambda x : 'Child' if x <=15 else 'Adult' )
print(titanic_df[['Age','Child_Adult']].head(8))

titanic_df['Age_cat'] = titanic_df['Age'].apply(lambda x : 'Child' if x<=15 else ('Adult' if x <= 60 else 'Elderly'))
print(titanic_df['Age_cat'].value_counts())

# 나이에 따라 세분화된 분류를 수행하는 함수 생성. 
def get_category(age):
    cat = ''
    if age <= 5: cat = 'Baby'
    elif age <= 12: cat = 'Child'
    elif age <= 18: cat = 'Teenager'
    elif age <= 25: cat = 'Student'
    elif age <= 35: cat = 'Young Adult'
    elif age <= 60: cat = 'Adult'
    else : cat = 'Elderly'
 
    return cat

# lambda 식에 위에서 생성한 get_category( ) 함수를 반환값으로 지정. 
# get_category(X)는 입력값으로 ‘Age’ 칼럼 값을 받아서 해당하는 cat 반환
# *cat = category
titanic_df['Age_cat'] = titanic_df['Age'].apply(lambda x : get_category(x))
print(titanic_df[['Age','Age_cat']].head())
