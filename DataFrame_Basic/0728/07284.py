from wordcloud import WordCloud
import matplotlib.pyplot as plt

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
df = pd.read_csv('./debate_transcript.csv')