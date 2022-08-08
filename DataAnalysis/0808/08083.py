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

# https://github.com/CSSEGISandData/COVID-19

doc = pd.read_csv('./csse_covid_19_data/csse_covid_19_daily_reports/04-01-2020.csv', encoding = 'utf-8') # error_bad_lines = False -> 에러 무시)
# print(doc.head())
# print(doc.shape)
# print(doc.columns)

# plt.figure(figsize=(5,5))
# sns.heatmap(data = doc.corr(), annot=True, fmt = '.2f', linewidths=0.5, cmap='Blues')
# plt.show()

countries = doc['Country_Region']
covid_stat = doc[['Confirmed', 'Deaths', 'Recovered']]
doc_us = doc[doc['Country_Region'] == 'US']
doc = doc.dropna(subset=['Confirmed'])
nan_data = {'Deaths': 0, 'Recovered':0}
doc = doc.fillna(nan_data)
# print(doc.head())