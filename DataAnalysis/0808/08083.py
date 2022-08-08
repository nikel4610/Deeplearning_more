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

doc = pd.read_csv('./COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/04-01-2020.csv', encoding = 'utf-8')
# print(doc.head())

