from konlpy.tag import _okt
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd
import numpy as np

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

