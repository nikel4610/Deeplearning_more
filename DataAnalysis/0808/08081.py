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

edu_col = ['Q4', 'Q6', 'Q15']
ds_col = ['Q5', 'Q20', 'Q22']

lg_col = ['Q8', 'Q11']
mon_col = ['Q24', 'Q25']

new_data = data[edu_col + ds_col]
new_data2 = data[lg_col + mon_col]

final_data = new_data.dropna()
final_data2 = new_data2.dropna()

# print(final_data.head())
# print(final_data2.head())

# # Q4 col pie chart
# Q4 = final_data["Q4"][1:]
# plt.figure(figsize=(16, 16))
# plt.pie(Q4.value_counts(),
#         labels=Q4.value_counts().index,
#         autopct='%d%%',
#         startangle=90,
#         textprops={'fontsize':12})
# plt.axis('equal')
# plt.title("Pie chart for Q4 column", fontsize=16)
# plt.show()

# # Q6 col pie chart
# Q6 = final_data["Q6"][1:]
# plt.figure(figsize=(24, 24))
# plt.pie(Q6.value_counts(),
#         labels=Q6.value_counts().index,
#         autopct='%d%%',
#         textprops={'fontsize':24})
# plt.axis('equal')
# plt.title("Pie chart for Q6 column", fontsize=48)
# plt.show()

# # Q15 col pie chart
# Q15 = final_data["Q15"][1:]
# plt.figure(figsize=(8,8))
# plt.pie(Q15.value_counts(),
#         labels=Q15.value_counts().index,
#         autopct='%d%%',
#         colors=sns.color_palette('hls',len(Q15.value_counts().index)),
#         textprops={'fontsize':12})
# plt.axis('equal')
# plt.title("Pie chart for Q15 column", fontsize=16, pad=50)
# plt.show()

# # Q5 col pie chart
# Q5 = final_data["Q5"][1:]
# plt.figure(figsize=(16, 16))
# plt.pie(Q5.value_counts(),
#         labels=Q5.value_counts().index,
#         autopct='%d%%',
#         textprops={'fontsize':24})
# plt.axis('equal')
# plt.title("Pie chart for Q5 column", fontsize=48, pad=50)
# plt.show()

# # Q20 col pie chart
# Q20 = final_data["Q20"][1:]
# plt.figure(figsize=(8,8))
# plt.pie(Q20.value_counts(),
#         labels=Q20.value_counts().index,
#         autopct='%d%%',
#         colors=sns.color_palette('hls',len(Q20.value_counts().index)),
#         textprops={'fontsize':16})
# plt.axis('equal')
# plt.title("Pie chart for Q20 column", fontsize=32, pad=50)
# plt.show()

# # Q22 col pie chart
# Q22 = final_data["Q22"][1:]
# plt.figure(figsize=(12, 12))
# plt.pie(Q22.value_counts(),
#         labels=Q22.value_counts().index,
#         autopct='%.2f%%',
#         colors=sns.color_palette('hls',len(Q22.value_counts().index)),
#         textprops={'fontsize':12})
# plt.axis('equal')
# plt.title("Pie chart for Q22 column", fontsize=32, pad=50)
# plt.show()

# set(data["Q3"])
# skorea = data[data["Q3"].isin(["Republic of Korea", "South Korea"])]
# sQ4 = skorea["Q4"]

# sns.countplot(y="Q4", data=skorea[1:])
# plt.show()

# plt.figure(figsize=(12, 12))
# plt.pie(sQ4.value_counts(),
#         labels=sQ4.value_counts().index,
#         autopct='%.2f%%',
#         colors=sns.color_palette('hls',len(sQ4.value_counts().index)),
#         textprops={'fontsize':12})
# plt.axis('equal')
# plt.title("Pie chart for Q4 column in South Korea", fontsize=32, pad=50)
# plt.show()

# https://www.kaggle.com/code/subinium/kaggle-2020-visualization-analysis/notebook

# Q2 Analysis
data['Q2'] = data['Q2'].apply(lambda x : 'ETC' if x not in ['Man', 'Woman'] else x)
data_q1q2 = data[data['Q2'] != 'ETC'].groupby(['Q2'])['Q1'].value_counts().unstack().sort_index()
man = data_q1q2.loc['Man']
woman = -data_q1q2.loc['Woman']

fig, ax = plt.subplots(1,1, figsize=(15, 6))
ax.bar(man.index, man, width=0.55, color='#004c70', alpha=0.8, label='Male')
ax.bar(woman.index, woman, width=0.55, color='#990000', alpha=0.8, label='Female')
ax.set_ylim(-1200, 3500)

for i in man.index:
    ax.annotate(f"{man[i]}", 
                   xy=(i, man[i] + 100),
                   va = 'center', ha='center',fontweight='light', fontfamily='serif',
                   color='#4a4a4a')
    
for i in woman.index:
    ax.annotate(f"{-woman[i]}", 
                   xy=(i, woman[i] - 100),
                   va = 'center', ha='center',fontweight='light', fontfamily='serif',
                   color='#4a4a4a')    

for s in ['top', 'left', 'right', 'bottom']:
    ax.spines[s].set_visible(False)

ax.set_xticklabels(data_q1q2.columns, fontfamily='serif')
ax.set_yticks([])    
ax.legend()
fig.text(0.16, 0.95, 'Age / Gender Distribution', fontsize=15, fontweight='bold', fontfamily='serif')    
plt.show()