# 앤스콤 4분할 그래프틑 데이터를 시각화하지 않고 수치만 확인하여 데이터 분석을 수행하면 잘못된 판단을 할 수 있다는것을 알려주는 예시이다
# 4개의 데이터 그룹의 평균, 분산이 각각 같고 상관관계, 회귀선이 같다
# 4개 데이터 그룹의 데이터가 동일할것이라고 착각할 수 있지만, 시각화하면 데이터 패턴이 서로 다르다.

import seaborn as sns
import matplotlib.pyplot as plt

# anscombe = sns.load_dataset('anscombe')

# dataset1 = anscombe[anscombe['dataset'] == 'I']
# dataset2 = anscombe[anscombe['dataset'] == 'II']
# dataset3 = anscombe[anscombe['dataset'] == 'III']
# dataset4 = anscombe[anscombe['dataset'] == 'IV']

# fig = plt.figure()
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)

# ax1.set_title('dataset1')
# ax2.set_title('dataset2')
# ax3.set_title('dataset3')
# ax4.set_title('dataset4')

# fig.suptitle('Anscombe Dataset')
# fig.tight_layout()

# ax1.plot(dataset1['x'], dataset1['y'])
# ax1.plot(dataset1['x'], dataset1['y'], 'o')

# ax2.plot(dataset2['x'], dataset2['y'])
# ax2.plot(dataset2['x'], dataset2['y'], 'o')

# ax3.plot(dataset3['x'], dataset3['y'])
# ax3.plot(dataset3['x'], dataset3['y'], 'o')

# ax4.plot(dataset4['x'], dataset4['y'])
# ax4.plot(dataset4['x'], dataset4['y'], 'o')

# plt.show()

# plt.plot([1, 2, 3, 4], [2, 3, 5, 10], label='Price ($)')
# plt.plot([1, 2, 3, 4], [3, 5, 9, 7], label='Demand (#)')
# plt.xlabel('X-Axis')
# plt.ylabel('Y-Axis')
# # plt.legend(loc='best') # ncol = 1
# plt.legend(loc='best', ncol=2, fontsize=14, frameon=True, shadow=True)
# plt.show()

# plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
# plt.xlabel('X-Axis')
# plt.ylabel('Y-Axis')
# # plt.xlim([0, 5]) # X축의 범위: [xmin, xmax]
# # plt.ylim([0, 20]) # Y축의 범위: [ymin, ymax]
# plt.axis([0, 5, 0, 20]) # X, Y축의 범위: [xmin, xmax, ymin, ymax]
# # plt.axis('square')
# plt.axis('scaled')
# plt.show()

# 히스토그램: 데이터의 분포와 빈도를 살펴보는 용도로 사용되는 그래프
# 일변량, 이변량, 다변량 그래프

tips = sns.load_dataset('tips')

# fig = plt.figure()
# ax1 = fig.add_subplot(1, 1, 1)
# ax1.scatter(tips['total_bill'], tips['tip']) # x축 간격 조정
# ax1.set_xlabel('Total Bill')
# ax1.set_ylabel('Tip')
# ax1.set_title('Total Bill vs Tip Scatter Plot')
# plt.show()

# 박스 그래프는 이산형 변수와 연속형 변수를 함께 사용할 수 있는 그래프
# 이산형 변수: 여러 개의 데이터를 하나의 변수로 묶어서 사용하는 경우
# 연속형 변수: 여러 개의 데이터를 연결하여 사용하는 경우

# fig = plt.figure()
# ax1 = fig.add_subplot(1, 1, 1)
# ax1.boxplot([tips[tips['sex'] =='Female']['tip'], tips[tips['sex'] =='Male']['tip']], labels=['Female', 'Male'])
# ax1.set_xlabel('Sex')
# ax1.set_ylabel('Tip')
# ax1.set_title('Boxplot of Tip by Sex')
# plt.show()

# # TotalBill, Tip, Sex 다변량 그래프
# # 성별이 여자면 1, 남자면 0 반환
# def recode_sex(sex):
#     if sex == 'Female':
#         return 1
#     else:
#         return 0

# tips['sex_color'] = tips['sex'].apply(recode_sex)

fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)

# # s는 점의 크기, c는 color
# ax1.scatter(x = tips['total_bill'], y = tips['tip'], s = tips['size'] * 10, c = tips['sex_color'], alpha = 0.5)
# ax1.set_xlabel('Total Bill')
# ax1.set_ylabel('Tip')
# ax1.set_title('Total Bill vs Tip Color by Sex and Sized by Size')
# plt.show()

# distplot(): 히스토그램 + 밀집도를 같이 표현
# ax = plt.subplots()

# # kde: 밀집도 그래프 설정
# ax = sns.distplot(tips['total_bill'], kde = True)
# ax.set_xlabel('Total Bill')
# ax.set_ylabel('Frequency')
# ax.set_title('Total Bill Histogram')
# plt.show()

# # rug = True: 그래프 축에 동일한 길이의 직선을 붙어 데이터의 밀집 정도를 표현
# ax = sns.distplot(tips['total_bill'], rug = True)
# ax.set_xlabel('Total Bill')
# ax.set_ylabel('Frequency')
# ax.set_title('Total Bill Histogram')
# plt.show()

# # countplot(): 이산값 표현 그래프
# ax = plt.subplots()
# ax = sns.countplot('day', data = tips)
# ax.set_title('Countplot of Days')
# ax.set_xlabel('Day of the Week')
# ax.set_ylabel('Frequency')
# plt.show()

# # regplot(): 산점도 + 회귀선 그래프 / fit_reg = False: 회귀선 제거
# ax = plt.subplots()
# ax = sns.regplot(x = 'total_bill', y = 'tip', data = tips)
# ax.set_title('Scatter Plot of Total Bill vs Tip')
# ax.set_xlabel('Total Bill')
# ax.set_ylabel('Tip')
# plt.show()

# # jointplot(): 산점도 + 히스토그램을 함께 표현
# ax = plt.subplots()
# ax = sns.jointplot(x = 'total_bill', y = 'tip', data = tips, kind = 'hex') # 육각형으로 데이터를 쌓아 표현하는 그래프
# ax.fig.suptitle('Jointplot of Total Bill and Tip', fontsize=10, y=1.03)
# ax.set_axis_labels(xlabel='Total Bill', ylabel ='Tip' )
# plt.show()

# # kdeplot(): 이차원 밀집도 표현 그래프
# ax = plt.subplots()
# ax = sns.kdeplot(data = tips['total_bill'], data2 = tips['tip'], shade = True) # shade = True: 음영 효과로 밀집도 표현
# ax.set_title('KDE Plot of Total Bill and Tip')
# ax.set_xlabel('Total Bill')
# ax.set_ylabel('Tip')
# plt.show()

# # barplot(): 지정한 변수의 평균을 계산해서 그래프에 표현 가능
# # 시간에 따라 지불한 비용의 평균을 barplot으로 표현
# ax = plt.subplots()
# ax = sns.barplot(x = 'time', y = 'total_bill', data = tips)
# ax.set_title('Bar Plot of average Total Bill and Time of day')
# ax.set_xlabel('Average Total Bill')
# ax.set_ylabel('Time of day')
# plt.show()

# # boxplot(): 최소값, 1분위값, 중앙값, 3분위값, 최대값, 이상치 등 통계량을 한번에 표현
# ax = plt.subplots()
# ax = sns.boxplot(x = 'time', y = 'total_bill', data = tips)
# ax.set_title('Box Plot of average Total Bill and Time of day')
# ax.set_xlabel('Total Bill')
# ax.set_ylabel('Time of day')
# plt.show()

# # violinplot(): boxplot에 커널 밀도를 추정하여 데이터 분산을 조금 더 정밀하게 표현한 그래프
# ax = plt.subplots()
# ax = sns.violinplot(x = 'time', y = 'total_bill', data = tips)
# ax.set_title('Box Plot of average Total Bill and Time of day')
# ax.set_xlabel('Total Bill')
# ax.set_ylabel('Time of day')
# plt.show()

# pairplot(): 관계 그래프
ax = sns.pairplot(tips)

# # map_upper(): 대각선 기준으로 위쪽에 그릴 그래프 지정
# # map_lower(): 대각선 기준으로 아래쪽에 그릴 그래프 지정
# # 대각선 기준으로 아래쪽에 이차원 밀집도
# # 대각선 기준으로 위쪽에 이차원 산점도
# pair_grid = sns.PairGrid(tips)
# pair_grid.map_upper(sns.regplot)
# pair_grid.map_lower(sns.kdeplot)
# pair_grid.map_diag(sns.distplot, rug = True)
# plt.show()

# # hue인수에 사용할 색상 열 이름 설정
# ax = plt.subplots()
# ax = sns.violinplot(x = 'time', y = 'total_bill' , hue = 'sex' , data = tips, split = True)  
# ax.set_title('Violinplot of average Total Bill for time of day')
# ax.set_xlabel('Time of Day')
# ax.set_ylabel('Total Bill')
# plt.show()

# ax = plt.subplots()
# ax = sns.lmplot(x = 'total_bill', y = 'tip' , hue = 'sex' , data = tips, fit_reg = False) 
# plt.show()

