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

df = pd.read_csv('./제주특별자치도_9시장별소비패턴현황_20170216.csv', encoding = 'cp949')
# print(df.head())

df_2014 = df[df['기준년도'] == 2014]
df_2015 = df[df['기준년도'] == 2015]
df_2016 = df[df['기준년도'] == 2016]

fig = plt.figure()
ax = fig.add_subplot(1,3,1)
ax2 = fig.add_subplot(1,3,2)
ax3 = fig.add_subplot(1,3,3)

df_2014_market = df_2014['시장명'][:]
ax.plot(df_2014_market, df_2014['20대 이하'], 'r', label=('20대 이하'))
ax.plot(df_2014_market, df_2014['30대'], 'g', label=('30대'))
ax.plot(df_2014_market, df_2014['40대'], 'b', label=('40대'))
ax.plot(df_2014_market, df_2014['50대 이상'], 'y', label=('50대 이상'))

ax.set_xlabel('시장')
ax.set_ylabel('사용한 금액')
ax.set_title('2014')
ax.set_xticklabels(df_2014_market, rotation = 90)
ax.legend()
ax.grid()

#############################################################################################

df_2015_market = df_2015['시장명'][:]
ax2.plot(df_2015_market, df_2015['20대 이하'], 'r', label=('20대 이하'))
ax2.plot(df_2015_market, df_2015['30대'], 'g', label=('30대'))
ax2.plot(df_2015_market, df_2015['40대'], 'b', label=('40대'))
ax2.plot(df_2015_market, df_2015['50대 이상'], 'y', label=('50대 이상'))

ax2.set_xlabel('시장')
ax2.set_ylabel('사용한 금액')
ax2.set_title('2015')
ax2.set_xticklabels(df_2015_market, rotation = 90)
ax2.legend()
ax2.grid()

##############################################################################################

df_2016_market = df_2016['시장명'][:]
ax3.plot(df_2016_market, df_2016['20대 이하'], 'r', label=('20대 이하'))
ax3.plot(df_2016_market, df_2016['30대'], 'g', label=('30대'))
ax3.plot(df_2016_market, df_2016['40대'], 'b', label=('40대'))
ax3.plot(df_2016_market, df_2016['50대 이상'], 'y', label=('50대 이상'))

ax3.set_xlabel('시장')
ax3.set_ylabel('사용한 금액')
ax3.set_title('2016')
ax3.set_xticklabels(df_2016_market, rotation = 90)
ax3.legend()
ax3.grid()

plt.show()