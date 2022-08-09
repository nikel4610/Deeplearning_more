import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from  matplotlib import font_manager, rc
import matplotlib.colors as mcolors
import math
import seaborn as sns

font_path="C://Windows//Fonts//malgun.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font)
plt.rcParams['axes.unicode_minus'] = False

# path = ('./csse_covid_19_data/csse_covid_19_daily_reports/')
# doc = pd.read_csv(path + '04-01-2020.csv', encoding = 'utf-8-sig') # error_bad_lines = False -> 에러 무시)
# # print(doc.head())
# # print(doc.shape)
# # print(doc.columns)

# # plt.figure(figsize=(5,5))
# # sns.heatmap(data = doc.corr(), annot=True, fmt = '.2f', linewidths=0.5, cmap='Blues')
# # plt.show()

# countries = doc['Country_Region']
# covid_stat = doc[['Confirmed', 'Deaths', 'Recovered']]
# doc_us = doc[doc['Country_Region'] == 'US']
# doc.isnull().sum()
# doc = doc.dropna(subset=['Confirmed'])
# nan_data = {'Deaths': 0, 'Recovered':0}
# doc = doc.fillna(nan_data)
# # print(doc.head())

# doc = doc.groupby('Country_Region').sum() # groupby 사용한 부분은 인덱스로 빠진다
# # print(doc[doc.index == 'US']) # 인덱스 값 확인
# print(doc.head())
# doc = doc[['Country/Region', 'Confirmed']] # 필요한 컬럼만 선택
# doc = doc.dropna(subset=['Confirmed']) # 특정 컬럼에 없는 데이터 삭제
# doc = doc.astype({'Confirmed': 'int64'}) # 특정 컬럼의 데이터 타입 변경

# doc.columns = ['Country_Region', 'Confirmed']

# print(doc.head())

doc = pd.read_csv("./COVID-19-master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv", encoding='utf-8-sig')
doc = doc[['iso2', 'Country_Region']]
# print(doc.head())
# print(doc.duplicated())
doc[doc.duplicated()]
doc = doc.drop_duplicates(subset='Country_Region', keep='last')
print(doc.head())