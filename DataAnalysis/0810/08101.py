import pandas as pd
import json
import os

PATH = "./COVID-19-master/csse_covid_19_data/csse_covid_19_2022/"
doc = pd.read_csv(PATH + "01-01-2022.csv", encoding='utf-8-sig')
# print(doc.head())

country_info = pd.read_csv("./COVID-19-master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv", encoding='utf-8-sig') # 나라 정보 csv

def create_dateframe(filename):
    doc = pd.read_csv(PATH + filename, encoding='utf-8-sig') # 1. csv 파일 읽기
    # China 컬럼만 추출
    doc = doc[doc['Country_Region'] == 'China']
    doc = doc[['Province_State', 'Deaths']] # 2. 특정 컬럼만 선택해서 데이터프레임 만들기
    doc = doc.dropna(subset=['Deaths']) # 3. 특정 컬럼에 없는 데이터 삭제하기    
    doc = doc.astype({'Deaths': 'int64'}) # 5. 특정 컬럼의 데이터 타입 변경하기
    doc = doc.groupby('Province_State').sum() # 6. 특정 컬럼으로 중복된 데이터를 합치기 -> 인덱스로 빠진다

    # 7. 파일명을 기반으로 날짜 문자열 변환하고, 'Deaths' 컬럼명 변경하기
    date_column = filename.split(".")[0].lstrip('0').replace('-', '/') # 날짜 문자열 변경
    doc.columns = [date_column] # 컬럼 이름 변경
    return doc

# 폴더 안의 모든 파일 읽기
def generate_dateframe_by_path(PATH):
    file_list, csv_list = os.listdir(PATH), list()
    first_doc = True
    for file in file_list:
        # csv 파일만 추가하기
        if file.split(".")[-1] == 'csv':
            csv_list.append(file)
    csv_list.sort()

    for file in csv_list:
        doc = create_dateframe(file)
        if first_doc:
            # 첫번째 파일은 하나밖에 없어서 False로 설정
            final_doc, first_doc = doc, False
        else:
            final_doc = pd.merge(final_doc, doc, how='outer', left_index=True, right_index=True)

    final_doc = final_doc.fillna(0)
    return final_doc

doc = generate_dateframe_by_path(PATH)
# print(doc.head())
doc = doc.astype('int64')
doc.to_csv("./COVID-19-master/final_df_Deaths_china.csv")