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

