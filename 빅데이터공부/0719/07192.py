import pandas as pd
from IPython.display import display 

titanic_df = pd.read_csv('titanic_train.csv')

pd.set_option('display.max_colwidth', 200)
titanic_df = pd.read_csv('titanic_train.csv')
titanic_boolean = titanic_df[titanic_df['Age'] > 60]
print(type(titanic_boolean))
print(titanic_boolean)

print(titanic_df[titanic_df['Age'] > 60][['Name','Age']].head(3))
print(titanic_df.loc[titanic_df['Age'] > 60, ['Name','Age']].head(3))
print(titanic_df[ (titanic_df['Age'] > 60) & (titanic_df['Pclass']==1) & (titanic_df['Sex']=='female')])

cond1 = titanic_df['Age'] > 60
cond2 = titanic_df['Pclass']==1
cond3 = titanic_df['Sex']=='female'
print(titanic_df[ cond1 & cond2 & cond3])
