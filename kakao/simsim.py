from konlpy.tag import _okt
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd
import numpy as np
from collections import Counter
import folium
import warnings
from glob import glob
import seaborn as sns
from  matplotlib import font_manager, rc
import thiswordnono

okt = _okt.Okt()

font_path="C://Windows//Fonts//malgun.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font)
plt.rcParams['axes.unicode_minus'] = False

with open('./KakaoTalk_20220803_1812_45_115_group.txt', 'r', encoding = 'utf-8') as f:
    text = f.read()

n_adj = []
for word, tag in okt.pos(text):
    if tag == 'Noun' or tag == 'Adjective':
        n_adj.append(word)

n_adj_no_stop = [word for word in n_adj if word not in thiswordnono.stopwords]
n_adj_no_stop = [word for word in n_adj_no_stop if len(word) >= 2]

# 가장 많은 단어를 10개 출력 후 그래프로 그리기
count = Counter(n_adj_no_stop)
count_10 = count.most_common(20)
# print(count_10)

plt.figure()
plt.bar(range(len(count_10)), [count_10[i][1] for i in range(len(count_10))], align='center')
plt.xticks(range(len(count_10)), [count_10[i][0] for i in range(len(count_10))])
plt.title('카카오톡 자주 사용한 단어 top10')
plt.xlabel('단어')
plt.ylabel('빈도수')
plt.show()


