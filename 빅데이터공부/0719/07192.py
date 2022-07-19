import pandas as pd
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

# Aggregation 함수, Sort 정렬
# 이름으로 정렬
titanic_sorted = titanic_df.sort_values(by=['Name'])
print(titanic_sorted.head(3))

# Pclass와 Name으로 내림차순 정렬
titanic_sorted = titanic_df.sort_values(by=['Pclass', 'Name'], ascending=False)
print(titanic_sorted.head(3))

print(titanic_df[['Age', 'Fare']].mean())
print(titanic_df[['Age', 'Fare']].sum())
print(titanic_df[['Age', 'Fare']].count())

titanic_groupby = titanic_df.groupby(by='Pclass')
print(type(titanic_groupby))

print(titanic_groupby[['Age', 'Fare']])
print(titanic_groupby[['Age', 'Fare']].count())

titanic_groupby = titanic_df.groupby('Pclass').count()
print(titanic_groupby)

titanic_groupby = titanic_df.groupby('Pclass')[['PassengerId', 'Survived']].count()
print(titanic_groupby)

# titanic_df.groupby('Pclass')['Age'].max(), titanic_df.groupby('Pclass')['Age'].min()
print(titanic_df.groupby('Pclass')['Age'].agg([max, min]))

agg_format={'Age':'max', 'SibSp':'sum', 'Fare':'mean'}
print(titanic_df.groupby('Pclass').agg(agg_format))

print(titanic_df.groupby(['Pclass']).agg(age_max=('Age', 'max'), age_mean=('Age', 'mean'), fare_mean=('Fare', 'mean')))

print(
titanic_df.groupby('Pclass').agg(
 age_max=pd.NamedAgg(column='Age', aggfunc='max'),
 age_mean=pd.NamedAgg(column='Age', aggfunc='mean'),
 fare_mean=pd.NamedAgg(column='Fare', aggfunc='mean')
)
)