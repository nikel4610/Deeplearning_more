from itertools import count
import pandas as pd
import datetime

df_confirmed = pd.read_csv("./COVID-19-master/final_df_Deaths_2022.csv")
# df_confirmed.head()

country_info = pd.read_csv("./COVID-19-master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv", encoding='utf-8-sig',
                           keep_default_na = False, na_values = '')
country_info = country_info[['iso2', 'Country_Region']]
country_info = country_info.drop_duplicates(subset='Country_Region', keep='first')
# print(country_info)

# 소문자로 바꾸기
country_info['iso2'] = country_info['iso2'].str.lower()
doc_final_country = pd.merge(df_confirmed, country_info, how='left', on='Country_Region')
# print(doc_final_country.head())

# null값 제거
doc_final_country = doc_final_country.dropna(subset=['iso2'])
# print(doc_final_country[doc_final_country['iso2'].isnull()])

def create_flag_link(row):
    flag_link = 'https://flagcdn.com/48x36/' + row + '.png'
    return flag_link

doc_final_country['iso2'] = doc_final_country['iso2'].apply(create_flag_link)

# 컬럼명을 리스트로 변경
cols = doc_final_country.columns.tolist()
cols.remove('iso2')
cols.insert(1, 'iso2')
doc_final_country = doc_final_country[cols]
# print(doc_final_country.head())

# 컬럼명 변경
cols[1] = 'Country_Flag'
doc_final_country.columns = cols
doc_final_country.to_csv("./COVID-19-master/final_covid_data_for_graph_Deaths.csv")