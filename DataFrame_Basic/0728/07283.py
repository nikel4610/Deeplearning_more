import matplotlib.pyplot as plt
import pandas as pd
import datetime

df = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/youtube.csv",index_col=0)

# 인기 동영상 제작 횟수가 많은 채널 상위 10개출력 (날짜 기준, 중복 포함)
print(df.groupby('channelTitle')['view_count'].sum().sort_values(ascending=False).head(10))

# dislikes수가 likes수보다 높은 동영상을 제작한 채널을 모두 출력
print(df[df['likes'] < df['dislikes']]['channelTitle'].unique())

# 채널명을 한번이라도 바꾼 채널의 개수 출력
result = df[['channelId', 'channelTitle']].drop_duplicates().channelId.value_counts()
result = result > 1
print(result.sum(), '개의 채널이 이름을 바꾼 채널입니다.')

# 일요일에 인기 있었던 동영상들 중 가장 많은 영상 종류(categoryId)를 출력
df['trending_date2'] = pd.to_datetime(df['trending_date2'])
print(df[df['trending_date2'].dt.day_name() == 'Sunday']['categoryId'].value_counts())

# 요일별 인기 동영상들의 categoryId별 개수를 행 인덱스는 'categoryId'로 열 인덱스는 '요일'로 출력
df['trending_date2'] = pd.to_datetime(df['trending_date2'])
day = df.groupby([df['trending_date2'].dt.day_name(), 'categoryId']).size().unstack()
print(day)

# viewcount 대비 댓글수가 가장 높은 동영상 제목을 출력하시오 (view_count값이 0인 경우 제외)
target = df.loc[df.view_count > 0]
target['ratio'] = target['comment_count'] / target['view_count']
print(target.sort_values('ratio', ascending = False).head(1))

# likes 대비 dislikes의 수가 가장 적은 동영상의 제목을 출력하시오
target1 = df.loc[df.likes > 0]
target1['ratio'] = target1['likes'] / target1['dislikes']
print(target1.sort_values('ratio', ascending = True).head(1))

