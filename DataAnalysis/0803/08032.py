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

df = pd.read_csv('./11.csv', encoding = 'cp949')
a = df.iloc[:, range(1, len(df.columns))]
b = []

for i in range(1, 29):
    b.append(a.iloc[:, i + 1] - a.iloc[:, i])


plt.figure()
plt.title('전년도 대비 증감')
plt.xlabel('년도')
plt.ylabel('탄소 배출량')
plt.plot(b[0], 'r', label = '총배출량')
plt.plot(b[1], 'g', label = '순배출량')
plt.plot(b[2], 'b', label = '에너지')
plt.legend()
plt.show()

