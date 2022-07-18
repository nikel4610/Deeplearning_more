import matplotlib.pyplot as plt
import numpy as np

m = 10
sigma = 2
x1 = np.random.randn(10000)
x2 = m+sigma*np.random.randn(10000)

plt.figure(figsize = (10, 6))

# alpha : 반투명도
# bins : 박스의 개수
plt.hist(x1, bins=40, alpha=0.2, color='r', label='x1')
plt.hist(x2, bins=20, alpha=1, color='b', label='x2')
plt.show()