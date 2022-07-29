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

# 한글 자연어 처리 (konlpy): 형태소 분석기(Hannanum, Kkma, Komoran, Mecab, Okt 포함)

okt = _okt.Okt()
# sentence = '오늘 점심은 비빔면을 먹는게 좋을까요? 아니면 카레를 먹는게 좋을까요?'
# print(okt.morphs(sentence))
# print(okt.nouns(sentence))
# print(okt.phrases(sentence))

# with open('./lawkr.tst', 'r', encoding='utf-8') as f:
#     text = f.read()

# # 명사만 추출
# nouns = okt.nouns(text)
# words = [word for word in nouns if len(word) > 1]
# c = Counter(words) # 단어별 빈도수 처리, dict타입으로 반환

# wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', width = 400, height = 400, scale = 2.0, max_font_size = 250)
# gen = wc.generate_from_frequencies(c)
# plt.figure()
# plt.imshow(gen)
# wc.to_file('./헌법_워드클라우드.png')

# blog_text = open('./blog_text.txt', 'r', encoding='utf-8').read()
# line = okt.pos(blog_text)

# # 명사와 형용사 출력
# n_adj = []
# for word, tag in line:
#     if tag == 'Noun' or tag == 'Adjective':
#         n_adj.append(word)
# # print(n_adj)
# # print(len(n_adj))

# words = [word for word in n_adj if len(word) > 1]
# c = Counter(words)

# image_file = './alice_mask.png'

# # 이미지 파일을 읽어서 파이썬 실행환경 메모리에 이미지 객체로 생성 후 ndarray객체로 생성(수치 배열)
# mask = np.array(Image.open(image_file))

# wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', width = 400, height = 400, mask = mask, scale = 2.0, max_font_size = 250, background_color = 'white')
# gen = wc.generate_from_frequencies(c)
# plt.figure(figsize = (12, 12))
# plt.imshow(gen, interpolation = 'bilinear')
# plt.axis('off')
# wc.to_file('./블로그_워드클라우드.png')

# 지도 시각화 유형
# Dot Density Map: 지도 위에 데이터 분포를 점으로 표현
# Choropleth Map(Field Map): 지리적 영역 범위별 수치 데이터 값을 색으로 표현
# Symbol Map(Bubble Map): 지도의 특정 지점에 해당하는 수치 값을 symbol의 크기로 표현
# Connection Map(Flow Map): 지역 간 이동 경로 표현하는 시각화 지도

# 어떤 지도를 활용하느냐에 따라 시각적 분석 효과는 다르다

# # Map 클래스로 지도 로드, 범위는 location 속성
# m = folium.Map(location=[37.5502, 126.982], zoom_start = 12)

# folium.Marker(location = [37.5502, 126.982], popup = '서울', icon = folium.Icon(color = 'red', icon = 'star')).add_to(m)
# folium.CircleMarker(location = [37.5502, 126.982], radius = 100, popup = '서울', color = 'red', fill_color = 'red', fill_opacity = 0.5).add_to(m)
# m.save('./map.html')

# 하나 이상의 csv파일을 로드해서 하나의 dataframe객체로 병합
file_names= glob('./data/*.csv')

total = pd.DataFrame()
for file_name  in file_names:
    temp = pd.read_csv(file_name, encoding = 'utf-8')
    total = pd.concat([total, temp])

total.reset_index(inplace = True, drop = True)

# 분석에 필요한 컬럼 추출
data_columns = ['상가업소번호', '상호명','지점명', '상권업종대분류명', '상권업종중분류명', '시도명', '시군구명', '행정동명', '경도', '위도']
data = total[data_columns]

# 메모리 낭비를 줄이기 위해 사용하지 않을 변수 삭제
del total

# 상권업종중분류명이 "커피점/카페" 인 데이터 추출하고 인덱스 재설정
df_coffee = data[data['상권업종중분류명']=="커피점/카페"]
df_coffee.index = range(len(df_coffee))

# # 전국 커피전문점 점포 수 출력
# print('전국 커피전문점 점포 수:', len(df_coffee))

# 커피전문점 중에 "서울"에 위치하고 있는 점포만 추출하고, 점포 수 출력
df_seoul_coffee = df_coffee[df_coffee["시도명"]=="서울특별시"]
df_seoul_coffee.index = range(len(df_seoul_coffee))

# 스타벅스 상호를 가진 전국의 커피전문점 점포 추출, 점포 수 출력
df_starbucks = df_coffee[df_coffee["상호명"].str.contains("스타벅스")]
df_starbucks.index = range(len(df_starbucks))

# 서울에 있는 스타벅스 커피전문점 점포 추출, 점포 수 출력
df_seoul_starbucks = df_starbucks[df_starbucks["시도명"]=="서울특별시"]
df_seoul_starbucks .index = range(len(df_seoul_starbucks ))

# 서울에 있는 스타벅스 점포수를 구별로 출력
df_seoul_starbucks['시군구명'].value_counts()

# font_path="C://Windows//Fonts//malgun.TTF"
# font = font_manager.FontProperties(fname=font_path).get_name()
# plt.rc('font', family=font)

# #서울에 있는 구 단위 스타벅스 점포수를 barplot으로 시각화
# plt.figure(figsize = (10, 6))
# plt.title("서울 스타벅스 점포수", fontdict = {"fontsize" : 20 })
# plt.bar(df_seoul_starbucks['시군구명'].value_counts().index, df_seoul_starbucks['시군구명'].value_counts().values)
# plt.xticks(rotation = 'vertical')
# plt.savefig('starbucks_barplot.png')
# plt.show()

# plt.figure(figsize = (10, 6))
# sns.countplot(data = df_seoul_starbucks, y = '시군구명')
# plt.savefig('starbucks_countplot.png')
# plt.show()

# plt.figure(figsize = (8, 8))
# plt.pie( df_seoul_starbucks['시군구명'].value_counts().values,
#   labels=df_seoul_starbucks['시군구명'].value_counts().index,
#   autopct='%d%%',
#   colors=sns.color_palette('hls', len(df_seoul_starbucks['시군구명'].value_counts().index)),
#   textprops={'fontsize':12})
    
# plt.axis('equal')
# plt.title('Pie chart for Starbucks count', fontsize = 16, pad = 50)
# plt.savefig('starbucks_piechart.png')
# plt.show()

# df_seoul_starbucks[['지점명', '경도', '위도']] 데이터 추출해서 지도에 위치 표시
lat = df_seoul_starbucks['위도'].mean()
lon = df_seoul_starbucks['경도'].mean()

m = folium.Map(location=[lat, lon], zoom_start=12)

for i in df_seoul_starbucks.index:
    sub_lat = df_seoul_starbucks.loc[i, '위도']
    sub_lon = df_seoul_starbucks.loc[i, '경도']
    sub_name = df_seoul_starbucks.loc[i, '지점명']
    folium.Marker([sub_lat, sub_lon], popup = sub_name).add_to(m)
m.save('starbucks_map.html')