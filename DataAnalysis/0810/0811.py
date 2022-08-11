import pandas as pd
import os

seoul = pd.read_csv('./COVID-19-master\서울시 코로나19 확진자 발생동향.csv', encoding = 'cp949')

seoul = seoul[['서울시 기준일', '서울시 확진자', '서울시 사망', '전국 확진', '전국 사망']]
seoul = seoul.sort_values(by=['서울시 기준일'], ascending = True)

# seoul ratio
seoul['seoul_confirmed_ratio'] = seoul['서울시 확진자'] / seoul['전국 확진']
seoul['seoul_death_ratio'] = seoul['서울시 사망'] / seoul['전국 사망']

seoul = seoul.drop(seoul.index[0])

seoul.columns = ['date', 'seoul_confirmed', 'seoul_death', 'korea_confirmed', 'korea_death', 'seoul_confirmed_ratio', 'seoul_death_ratio']
seoul.to_csv('./COVID-19-master/seoul_confirmed_ratio.csv')



