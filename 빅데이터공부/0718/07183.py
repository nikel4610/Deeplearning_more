import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# m = 10
# sigma = 2
# x1 = np.random.randn(10000)
# x2 = m+sigma*np.random.randn(10000)

# plt.figure(figsize = (10, 6))

# # alpha : 반투명도
# # bins : 박스의 개수
# plt.hist(x1, bins=40, alpha=0.2, color='r', label='x1')
# plt.hist(x2, bins=20, alpha=1, color='b', label='x2')
# plt.show()

# y = [13, 15, 12, 16, 10, 11, 14, 12, 11, 15]
# y2 = [14, 20, 10, 21, 23, 14, 15, 2, 34, 12]
# plt.plot(range(len(y)), y, label = 'y')
# plt.plot(range(len(y2)), y2, label = 'y2')
# plt.xlabel('This is X')
# plt.ylabel('This is Y')
# plt.legend(loc = 'upper left')
# plt.show()

# x = np.random.rand(30)
# y = np.random.rand(30)
# colors = np.random.rand(30)
# shape = np.pi * (np.random.rand(30) * 20) ** 2
# plt.scatter(x, y, c=colors, s=shape, alpha=0.7, marker = '*')
# plt.show()

titanic_df = pd.read_csv('titanic_train.csv')
# print(type(titanic_df))
# print(titanic_df.head())
# print(titanic_df.tail())

# csv 파일의 모든 정보 다 보여줌
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_colwidth', 100)
pd.set_option('display.max_columns', 100)

dic1 = {'Name': ['Chulmin', 'Eunkyung','Jinwoong','Soobeom'],
 'Year': [2011, 2016, 2015, 2015],
 'Gender': ['Male', 'Female', 'Male', 'Male']
 }
# 딕셔너리를 DataFrame으로 변환
data_df = pd.DataFrame(dic1)
print(data_df)
print("#"*30)
# 새로운 컬럼명을 추가
data_df = pd.DataFrame(dic1, columns=["Name", "Year", "Gender", "Age"])
print(data_df)
print("#"*30)
# 인덱스를 새로운 값으로 할당. 
data_df = pd.DataFrame(dic1, index=['one','two','three','four'])
print(data_df)
print("#"*30)

titanic_df.info()
titanic_df.describe()

value_counts = titanic_df['Pclass'].value_counts()
print(value_counts)
titanic_df['Pclass'].head()
titanic_pclass = titanic_df['Pclass']
print(type(titanic_pclass))
print('titanic_df 데이터 건수:', titanic_df.shape[0])
print('기본 설정인 dropna=True로 value_counts()')

# value_counts()는 디폴트로 dropna=True 이므로 value_counts(dropna=True)와 동일. 
print(titanic_df['Embarked'].value_counts())
print(titanic_df['Embarked'].value_counts(dropna=False))

# DataFrame에서도 value_counts() 적용 가능. 
titanic_df[['Pclass', 'Embarked']].value_counts()
