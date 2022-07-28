from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import wordcloud
from sklearn.feature_extraction.text import CountVectorizer

# wordcloud: 핵심 키워드를 시각화(단어의 빈도수 기준 중요도를 시각화)
#            단어의 빈도수 계산해서 시각적으로 표현

# 한글 폰트 설정: font_path 인수에 ttf경로 이름
# 배경색 설정: background_color
# WordCloud 크기: width, height
# 최대 글자 수: max_words
# 최소 글자 수: min_word_length
# 최대 폰트 크기: max_font_size
# 불용어 설정: stopwords

# 2020년 대통령 선거를 위한 민주화 기본 토론 csv파일
df = pd.read_csv('./debate_transcripts.csv', encoding = 'cp1252')

text = df[df.speaker == 'Joe Biden'].speech.tolist()
text = ' '.join(text).lower()
wordcloud = WordCloud(stopwords = STOPWORDS, collocations = True).generate(text)
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis('off')
# plt.show()

# 빈도수 확인
# text_dictionary = wordcloud.process_text(text)
# word_freq = {k: v for k, v in sorted(text_dictionary.items(), reverse = True, key = lambda item: item[1])}
# rel_freq = wordcloud.words_

# sklearn.feature_extraction.text.CountVectorizer
# 단어들이 출현빈도로 여러 문서의 단어를 벡터화
speakers = df.speaker.unique()
corpus = [' '.join(df[(df.speaker == candidate)].speech.tolist()) for candidate in speakers]

cv = CountVectorizer(stop_words = STOPWORDS, ngram_range = (1, 3))
X = cv.fit_transform(corpus)