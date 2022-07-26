import numpy as np
import pandas as pd
import cx_Oracle

db = cx_Oracle.makedsn('localhost', 1521, 'xe')
conn = cx_Oracle.connect('system', '1234', db)

# sql을 수행한 결과 저장
cursor = conn.cursor()
cursor.execute("select * from emp")
datas = cursor.fetchall() # 리스트 반환
# print(datas)

# 데이터프레임으로 저장
datas_df = pd.DataFrame(datas)
# print(datas_df)

# column 이름 가져오기 -> 데이터 프레임에 저장
cursor.execute("select column_name from user_tab_columns where table_name = 'EMP'")
column_names = cursor.fetchall()
datas_df.columns = column_names
print(datas_df)



# 연결 끊기
cursor.close()
conn.close()

