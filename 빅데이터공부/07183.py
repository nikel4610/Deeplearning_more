import matplotlib.pyplot as plt
import numpy as np

# m = 10
# sigma = 2
# x1 = np.random.randn(10000)
# x2 = m+sigma*np.random.randn(10000)

# plt.figure(figsize = (10, 6))

# # alpha : 반투명도
# # bins : 박스의 개수
# plt.hist(x1, bins=40, alpha=0.2, color='r', label='x1')
# plt.hist(x2, bins=20, alpha=1, color='b', label='x2')
# plt.show()

# y = [13, 15, 12, 16, 10, 11, 14, 12, 11, 15]
# y2 = [14, 20, 10, 21, 23, 14, 15, 2, 34, 12]
# plt.plot(range(len(y)), y, label = 'y')
# plt.plot(range(len(y2)), y2, label = 'y2')
# plt.xlabel('This is X')
# plt.ylabel('This is Y')
# plt.legend(loc = 'upper left')
# plt.show()

x = np.random.rand(30)
y = np.random.rand(30)
colors = np.random.rand(30)
shape = np.pi * (np.random.rand(30) * 20) ** 2
plt.scatter(x, y, c=colors, s=shape, alpha=0.7, marker = '*')
plt.show()