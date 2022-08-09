import pandas as pd

df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'customer_id': [1, 2, 3],
    'customer_name': ['Robert', 'Peter', 'Dave']
}, columns=['id', 'customer_id', 'customer_name'])

df2 = pd.DataFrame({
    'id': [1, 2, 4],
    'order_id': [100, 200, 300],
    'order_date': ['2021-01-21', '2021-02-03', '2020-10-01']
}, columns=['id', 'order_id', 'order_date'])

# print(df1)
# print(df2)

# doc = pd.concat([df1, df2]) # default axis = 0 (위에서 아래로) / axis = 1 (왼쪽에서 오른쪽으로)
# print(doc.head())

# 두 df를 합치기
print(pd.merge(df1, df2)) # on = '칼럼명')
print('----------------------------------------------------')

# inner : 내부 조인 - SQL의 INNER JOIN 과 동일
# outer : 완전 외부 조인 - SQL의 OUTER JOIN 과 동일
# left : 왼쪽 우선 외부 조인 - SQL의 LEFT OUTER JOIN 과 동일
# right : 오른쪽 우선 외부 조인 - SQL의 RIGHT OUTER JOIN 과 동일

# default = inner
print(pd.merge(df1, df2, how = 'inner'))
print('----------------------------------------------------')

print(pd.merge(df1, df2, on='id', how='outer'))
print('----------------------------------------------------')

print(pd.merge(df1, df2, on='id', how='left'))
print('----------------------------------------------------')

print(pd.merge(df1, df2, on='id', how='right'))
print('----------------------------------------------------')

# 인덱스 기준으로 합치기
df1 = df1.set_index('id')
df2 = df2.set_index('id')

print(pd.merge(df1, df2, left_index=True, right_index=True))
print('----------------------------------------------------')

print(pd.merge(df1, df2, how='outer', left_index=True, right_index=True))
print('----------------------------------------------------')