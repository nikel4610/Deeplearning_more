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

data = pd.read_csv('./kaggle_survey_2020_responses.csv') # ,header = 1)
# print(data.head())

questions = data.iloc[0, :].T
data = data.iloc[1:, :]

fig, ax = plt.subplots(figsize=(16, 16))

lg_col = ['Q8', 'Q11']
mon_col = ['Q24', 'Q25']

new_data2 = data[lg_col + mon_col]
final_data2 = new_data2.dropna()

data_q24 = final_data2["Q24"][1:].value_counts().sort_index()
ax.bar(data_q24.index, data_q24.values, width=0.5, color='#ff7f0e')
ax.set_xticks(data_q24.index)
ax.set_xticklabels(data_q24.index, rotation=45)
ax.set_title("Q24", fontsize=24)
ax.set_xlabel("What is your current yearly compensation (approximate $USD)?", fontsize=24)
ax.set_ylabel("Count", fontsize=24)
plt.show()

# Q8 col pie chart
Q8 = final_data2["Q8"][1:]
plt.figure(figsize=(16, 16))
plt.pie(Q8.value_counts(),
        labels=Q8.value_counts().index,
        autopct='%d%%',
        startangle=90,
        textprops={'fontsize':12})
plt.axis('equal')
plt.title("What programming language would you recommend an aspiring data scientist to learn first?", fontsize=16)
plt.show()
