from konlpy.tag import _okt
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd
import numpy as np
from collections import Counter

# 한글 자연어 처리 (konlpy): 형태소 분석기(Hannanum, Kkma, Komoran, Mecab, Okt 포함)

okt = _okt.Okt()
# sentence = '오늘 점심은 비빔면을 먹는게 좋을까요? 아니면 카레를 먹는게 좋을까요?'
# print(okt.morphs(sentence))
# print(okt.nouns(sentence))
# print(okt.phrases(sentence))

with open('./lawkr.tst', 'r', encoding='utf-8') as f:
    text = f.read()

# 명사만 추출
nouns = okt.nouns(text)
words = [word for word in nouns if len(word) > 1]
c = Counter(words) # 단어별 빈도수 처리, dict타입으로 반환

wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', width = 400, height = 400, scale = 2.0, max_font_size = 250)
gen = wc.generate_from_frequencies(c)
plt.figure()
plt.imshow(gen)
wc.to_file('./헌법_워드클라우드.png')