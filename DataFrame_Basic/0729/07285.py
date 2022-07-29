import pandas as pd
import datetime

# # #월드컵 출전선수 골기록 데이터 1930 ~2018년도 월드컵 출전선수 골기록
# df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/worldcup/worldcupgoals.csv')

# # 전체기간동안 각 나라별 골득점수 상위 5개 국가와 그 득점수를 데이터프레임형태로 출력
# print(df.groupby('Country')['Goals'].sum().sort_values(ascending=False).head(5))

# # 전체기간동안 골득점을 한 선수가 가장 많은 나라 상위 5개 국가와 그 선수 숫자를 데이터 프레임 형식으로 출력
# print(df.groupby('Country').size().sort_values(ascending=False).head(5))

# # Years 컬럼은 년도 -년도 형식으로 구성되어있고, 각 년도는 4자리 숫자이다. 년도 표기가 4자리 숫자로 안된 케이스가 존재한다. 해당 건은 몇건인지 출력
# df['Year list'] = df['Years'].str.split('-')

# def checkFour(x):
#     for value in x:
#         if len(str(value)) != 4:
#             return False
#     return True

# df['check'] = df['Year list'].apply(checkFour)
# print(len(df[df['check'] == False]))

# # 월드컵 출전횟수를 나타내는 ‘LenCup’ 컬럼을 추가하고 4회 출전한 선수가 몇명인지 구하기
# df['LenCup'] = df['Year list'].apply(lambda x: len(x))
# print(df.groupby('Player')['LenCup'].sum().sort_values(ascending=False).value_counts()[4])

# # 2002년도에 출전한 전체 선수는 몇명인가?
# print(len(df[df['Years'].str.contains('2002')]))

# # 이름에 ‘carlos’ 단어가 들어가는 선수의 숫자는 몇 명인가?
# print(len(df[df['Player'].str.lower().str.contains('carlos')]))

# # 월드컵 출전 횟수가 1회뿐인 선수들 중에서 가장 많은 득점을 올렸던 선수는 누구인가? 
# print(df[df['LenCup'] == 1].sort_values('Goals', ascending=False).head(1))

# # 월드컵 출전횟수가 1회 뿐인 선수들이 가장 많은 국가는 어디인가?
# print(df[df['LenCup'] == 1].Country.value_counts().sort_values(ascending=False).head(1))

