import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from  matplotlib import font_manager, rc
import matplotlib.colors as mcolors
import math

font_path="C://Windows//Fonts//malgun.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font)
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('./제주특별자치도_개별관광(FIT)_증가에_따른_제주_관광객_소비패턴_변화_분석_BC카드_빅데이터_내국인관광객_20170216.csv', encoding = 'cp949')

df_2014 = df[df['기준년월'].str.contains('14')]
df_2015 = df[df['기준년월'].str.contains('15')]
df_2016 = df[df['기준년월'].str.contains('16')]

fig = plt.figure()
ax = fig.add_subplot(131)
ax2 =fig.add_subplot(132)
ax3 = fig.add_subplot(133)

df_2014_buy_count = df_2014['업종명'].value_counts()
df_2015_buy_count = df_2015['업종명'].value_counts()
df_2016_buy_count = df_2016['업종명'].value_counts()

ax.pie(df_2014_buy_count, labels=df_2014_buy_count.index, autopct='%1.1f%%', shadow=True, startangle=90)
ax2.pie(df_2015_buy_count, labels=df_2015_buy_count.index, autopct='%1.1f%%', shadow=True, startangle=90)
ax3.pie(df_2016_buy_count, labels=df_2016_buy_count.index, autopct='%1.1f%%', shadow=True, startangle=90)

# df_2014_age_count = df_2014['연령대별'].value_counts()
# df_2015_age_count = df_2015['연령대별'].value_counts()
# df_2016_age_count = df_2016['연령대별'].value_counts()

# ax.pie(df_2014_age_count, labels=df_2014_age_count.index, autopct='%1.1f%%', shadow=True, startangle=90)
# ax2.pie(df_2015_age_count, labels=df_2015_age_count.index, autopct='%1.1f%%', shadow=True, startangle=90)
# ax3.pie(df_2016_age_count, labels=df_2016_age_count.index, autopct='%1.1f%%', shadow=True, startangle=90)

ax.set_title('2014')
ax2.set_title('2015')
ax3.set_title('2016')

plt.axis('equal')
plt.show()