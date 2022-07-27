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

# df1 = pd.DataFrame({    '도시': ['서울', '서울', '서울', '부산', '부산'],
#     '연도': [2000, 2005, 2010, 2000, 2005],
#     '인구': [9853972, 9762546, 9631482, 3655437, 3512547]})

# df2 = pd.DataFrame(    np.arange(12).reshape((6, 2)),
#     index=[['부산', '부산', '서울', '서울', '서울', '서울'],
#            [2000, 2005, 2000, 2005, 2010, 2015]],
#     columns=['데이터1', '데이터2'])

# print(pd.merge(df1, df2, left_on = ['도시', '연도'], right_index = True))

# df1 = pd.DataFrame(
#     [[1., 2.], [3., 4.], [5., 6.]],
#     index=['a', 'c', 'e'],
#     columns=['서울', '부산'])

# df2 = pd.DataFrame(
#     [[7., 8.], [9., 10.], [11., 12.], [13, 14]],
#     index=['b', 'c', 'd', 'e'],
#     columns=['대구', '광주'])

# # outer 방식으로 merge, right_index, left_index 사용
# print(pd.merge(df1, df2, how = 'outer', left_index = True, right_index = True))
# print(df1.join(df2, how = 'outer'))

# df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/mergeTEst.csv',index_col= 0) 

# df1 = df.iloc[:4, :]
# df2 = df.iloc[4:, :]

# # df1과 df2를 하나의 데이터프레임으로 append 방식으로연결, 반환 결과 출력
# print(df1.append(df2))

# df3 = df.iloc[:2, :4]
# df4 = df.iloc[5:, 3:]

# # df3, df4의 데이터를 두 데이터프레임에 모두 포함되어 있는 년도에 대해서만 데이터를 연결, 반환 결과 출력
# print(pd.concat([df3, df4], join = 'inner'))

# # df3, df4 두 데이터프레임을 outer 방식으로 연결하고 결측치를 0으로 대체한 결과 출력
# print(pd.concat([df3, df4], join = 'outer').fillna(0))

# pivot(행 인덱스를 사용할 컬럼, 열 인덱스로 사용할 컬럼, 데이터로 사용할 열) 
# -> 데이터 컬럼 중에서 두개의 컬럼을 각각 행 인덱스, 열 인덱스로 사용해서 데이터를 조회하는 기능 (table 구조)

# data = {
#     "도시": ["서울", "서울", "서울", "부산", "부산", "부산", "인천", "인천"],
#     "연도": ["2015", "2010", "2005", "2015", "2010", "2005", "2015", "2010"],
#     "인구": [9904312, 9631482, 9762546, 3448737, 3393191, 3512547, 2890451, 263203],
#     "지역": ["수도권", "수도권", "수도권", "경상권", "경상권", "경상권", "수도권", "수도권"]
# }

# columns = ["도시", "연도", "인구", "지역"]
# df1 = pd.DataFrame(data, columns=columns)

# # 행 인덱스는 "도시", 열 인덱스는 "연도", 데이터는 "인구"로 pivot 테이블 생성
# print(df1.pivot(index = "도시", columns = "연도", values = "인구"))
# # print(df1.set_index(["도시", "연도"])[["인구"]].unstack())
# # 행 인덱스와 열 인덱스가 key 역할을 하므로, 조건을 만족하는 데이터가 2개 이상인 경우 ValueError 발생

# # print(df1.pivot(['지역', '도시']), '연도', '인구') # error

# # 국가별 5세 이하 사망비율 통계
# df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/under5MortalityRate.csv')

# # 'Indicator'열 삭제하고 'First Tooltip' 열에서 신뢰구간([]) 제거
# df.drop('Indicator', axis = 1, inplace = True)
# df['First Tooltip'] = df['First Tooltip'].map(lambda x: float(x.split("[")[0]))
# print(df.head(5))

# # 'Period'열이 2015 이상이고, 'Dim1'열이 'Both sexes'인 데이터를 추출하고, 지역을 행으로 년도별 사람들을 피벗테이블로 생성
# result = df[(df.Period >= 2015) & (df.Dim1 == 'Both sexes')]
# result.pivot(index = 'Location', columns = 'Period', values = 'First Tooltip')
# print(result)

# # 'Dim1'열을 행으로 년도별 사망 비율의 평균 구하기
# df.pivot_table(index = 'Dim1', columns = 'Period', values = 'First Tooltip', aggfunc = 'mean')
# print(df)

# #올림픽 메달리스트 정보 데이터
# df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/winter.csv')

# # 데이터에서 KOR 데이터만 추출하고, 년도에 따른 메달 개수를 pivot 테이블로 생성(메달 타입이 열 인덱스)
# print(df[df.Country == 'KOR'].pivot_table(index = 'Year', columns = 'Medal', aggfunc = 'size').fillna(0))

# # 전체 데이터에서 sport 종류에 따른 성별수를 pivot 테이블로 생성
# print(df.pivot_table(index = 'Sport', columns = 'Gender', aggfunc = 'size'))

# # 전체 데이터에서 Disipline 종류에 따른 Medal수를 pivot 테이블로 생성
# print(df.pivot_table(index = 'Discipline', columns = 'Medal', aggfunc = 'size'))


