import numpy as np
import pandas as pd

# # concat(): 연결하려는 데이터프레임을 리스트에 담아 전달하면 연결한 데이터프레임을 반환, 2개 이상의 데이터프레임을 연결
# #           연결할 데이터프레임은 append 방식으로 연결

# df1 = pd.DataFrame([['a0','a0','a0','a0'],['a1','a1','a1','a1'],
#                     ['a2','a2','a2','a2'], ['a3','a3','a3','a3']], columns=['A','B', 'C', 'D'])

# df2 = pd.DataFrame([['a4','a4','a4','a4'],['a5','a5','a5','a5'],
#                     ['a6','a6','a6','a6'], ['a7','a7','a7','a3']], columns=['A','B', 'C', 'D'])

# df3 = pd.DataFrame([['a8','a8','a8','a8'],['a9','a9','a9','a9'],
#                     ['a10','a10','a10','a10'], ['a11','a11','a11','a11']], columns=['A','B', 'C', 'D'])

# # row_concat = pd.concat([df1, df2, df3])
# # print(row_concat)

# new_row_series = pd.Series(['n1', 'n2', 'n3', 'n4'])
# # print(pd.concat([df1, new_row_series]))

# df2['E'] = ['n1', 'n2', 'n3', 'n4']
# # row_concat = pd.concat([df1, df2, df3])
# # print(row_concat)

# df2.drop(['E'], axis=1, inplace = True)

# # ['n1', 'n2', 'n3', 'n4']를 1개의 행으로 df1 데이터프레임에 연결
# new = pd.DataFrame([['n1', 'n2', 'n3', 'n4']], columns=['A', 'B', 'C', 'D'])
# # pd.concat([df1, new])
# df1.append(new)
# print(df1)

# data_dict = {'A' : 'n1', 'B' : 'n2', 'C' : 'n3', 'D' : 'n4'}
# df2.append(data_dict, ignore_index = True)
# print(df2)

# row_concat = pd.concat([df1, df2, df3], ignore_index = True)
# print(row_concat)

# # 열 인덱스가 정수 인덱스로 초기화됨
# col_concat = pd.concat([df1, df2, df3], axis=1, ignore_index = True)
# print(col_concat)

# df2.columns = ['E', 'F', 'G', 'H']
# df3.columns = ['A', 'C', 'F', 'H']
# print(pd.concat([df1, df2, df3]))

# # 공통 열 기준으로 연결
# print(pd.concat([df1, df3], join = 'inner'))

# df2.index = [4, 5, 6, 7]
# df3.index = [0, 2, 5, 7]
# print(pd.concat([df1, df2, df3], axis = 1))

# print(pd.concat([df1, df3], axis = 1, join = 'inner'))

# # merge(): inner join으로 실행
# # df1.merge(df2, left_on = /right_on =) 형식으로 사용됨

# df1 = pd.DataFrame({    '고객번호': [1001, 1002, 1003, 1004, 1005, 1006, 1007],
#                     '이름': ['둘리', '도우너', '또치', '길동', '희동', '마이콜', '영희']
#                       }, columns=['고객번호', '이름'])

# df2 = pd.DataFrame({ '고객번호': [1001, 1001, 1005, 1006, 1008, 1001],
#                      '금액': [10000, 20000, 15000, 5000, 100000, 30000]
#                     }, columns=['고객번호', '금액'])

# print(pd.merge(df1, df2))
# print(pd.merge(df1, df2, how = 'outer'))
# print(pd.merge(df1, df2, how = 'left'))
# print(pd.merge(df1, df2, how = 'right'))

# df1 = pd.DataFrame({
#     '고객명': ['춘향', '춘향', '몽룡'],
#     '날짜': ['2018-01-01', '2018-01-02', '2018-01-01'],
#     '데이터': ['20000', '30000', '100000']})

# df2 = pd.DataFrame({
#     '고객명': ['춘향', '몽룡'],
#     '데이터': ['여자', '남자']})

# print(pd.merge(df1, df2, on = '고객명'))

df1 = pd.DataFrame({    '이름': ['영희', '철수', '철수'],    '성적': [1, 2, 3]}  )
df2 = pd.DataFrame({    '성명': ['영희', '영희', '철수'],    '성적2': [4, 5, 6]}  )
