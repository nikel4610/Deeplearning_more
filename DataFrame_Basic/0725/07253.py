import numpy as np
import pandas as pd

# DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/lol.csv'

# df = pd.read_csv(DataUrl, sep='\t')
# print(type(df))

# # 5번째 컬럼명 출력
# print(df.columns[4])

# # 6번째 칼럼의 데이터 타입 출력
# print(df.dtypes[5])

# s0 = pd.Series([9904312, 3448737, 2890451, 2466052])
# print(s0.index)
# print(s0.values)
# s = pd.Series([9904312, 3448737, 2890451, 2466052], index=['서울', '부산', '대구', '인천'])
# print(s.index)
# print(s.values)

# # 라벨 인덱스 이름 지정
# s.name = '인구'
# s.index.name = '지역'
# print(s)

# print(s[3], s['부산'])
# print(s[:3], s['부산' : '대구'])
# print(type(s[:3])) # 슬라이싱으로 추출한 부분집합의 반환 타입
# print(s.부산) # 인덱스 이름을 사용하여 추출
# print('부산' in s) # True

# # dict로 부터 (key, value) 로 추출
# for k, v in s.items():
#     print('%s = %d'%(k, v))

# # 값 추가
# s['광주'] = 5123456
# print(s)

# # 값 제거
# del s['서울']
# print(s)

# s2 = pd.Series([9904312, 3448737, 2890451, 2466053], index=['서울', '부산', '대구', '인천'])
# print(s - s2)

# # 연산결과에서 null값이 아닌 값만 출력
# print((s - s2).dropna())

# DataFrame: 1개 이상의 Series가 열 단위로 결합된 2차원 구조
# -> Series[데이터 + index] + 행이름index
# DataFrame(2차원 데이터 객체, index=행 인덱스 배열, column = 열 인덱스 배열)
# ndarray, dict, dataframe, list, Series 객체로 부터 DataFrame 객체 생성 가능

datas = {"2015": [9904312, 3448737, 2890451, 2466053],
         "2016": [12156488, 10455588, 11856488, 12656488],
         "2017": [14256488, 13455588, 15856488, 14656488],
         "2018": [16256488, 15455588, 17856488, 16656488]}
index = ['서울', '부산', '대구', '인천']
columns = ['2015', '2016', '2017', '2018']

df1 = pd.DataFrame(datas, index = index, columns = columns)
print(df1.values)
print(df1.index)
print(df1.columns)

# columns, index 이름 추가
df1.columns.name = '년도'
df1.index.name = '지역'
print(df1)

# indexing, slicing
# DataFrame은 정수 인덱스의 슬라이싱은 행을 인덱싱할때만 사용 가능, 열 인덱싱은 사용 못함
print(df1[['2015']])
# print(df1[[0]]) # error
# print(df1[0]) # error

# 열 인덱스가 정수인덱스인 경우 추출 가능
df2 = pd.DataFrame(np.arange(12).reshape(3, 4))
print(df2)
print(df2[0])

# loc: 인덱스 이름을 사용하여 추출
# -> df.loc[행 인덱스, 열 인덱스]
# iloc: 정수 인덱스를 사용하여 추출
print(df1.iloc[0, 0])

# 6번재 컬럼의 세번째 데이터값 출력
