from konlpy.tag import _okt
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd
import numpy as np
from collections import Counter
import folium

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

# Map 클래스로 지도 로드, 범위는 location 속성
m = folium.Map(location=[37.5502, 126.982], zoom_start = 12)

folium.Marker(location = [37.5502, 126.982], popup = '서울', icon = folium.Icon(color = 'red', icon = 'star')).add_to(m)
folium.CircleMarker(location = [37.5502, 126.982], radius = 100, popup = '서울', color = 'red', fill_color = 'red', fill_opacity = 0.5).add_to(m)
m.save('./map.html')