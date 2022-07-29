import pandas as pd

# #월드컵 출전선수 골기록 데이터 1930 ~2018년도 월드컵 출전선수 골기록
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/worldcup/worldcupgoals.csv')

# 전체기간동안 각 나라별 골득점수 상위 5개 국가와 그 득점수를 데이터프레임형태로 출력
print(df.groupby('Country')['Goals'].sum().sort_values(ascending=False).head(5))

# 전체기간동안 골득점을 한 선수가 가장 많은 나라 상위 5개 국가와 그 선수 숫자를 데이터 프레임 형식으로 출력

# Years 컬럼은 년도 -년도 형식으로 구성되어있고, 각 년도는 4자리 숫자이다. 년도 표기가 4자리 숫자로 안된 케이스가 존재한다. 해당 건은 몇건인지 출력


# 월드컵 출전횟수를 나타내는 ‘LenCup’ 컬럼을 추가하고 4회 출전한 선수의 숫자 구하기


# 2002년도에 출전한 전체 선수는 몇명인가?

# 이름에 ‘carlos’ 단어가 들어가는 선수의 숫자는 몇 명인가?


# 월드컵 출전 횟수가 1회뿐인 선수들 중에서 가장 많은 득점을 올렸던 선수는 누구인가? 

# 월드컵 출전횟수가 1회 뿐인 선수들이 가장 많은 국가는 어디인가?