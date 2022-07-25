 # 3.9.7 base/conda
 # http://192.168.0.15:8080/python.html

import numpy as np

list3 = [[1, 2, 3, 4], 
         [5, 6, 7, 8], 
         [9, 10, 11, 12]]
arr3 = np.array(list3)

# 3, 8 출력
print(arr3[[0, 1], [2, 3]]) # [3 8]

print(arr3[0, : ]) # 0번째 행의 모든 열

bool_indexing = np.array([[True, False, True, False], [True, False, True, False], [True, False, True, False]])
n = arr3[bool_indexing]
print(n)  # [ 1  3  5  7  9 11]

bool_indexing2 = (arr3 % 2 == 0)
print(bool_indexing2)
n2 = arr3[bool_indexing2]
print(n2) # [ 2  4  6  8 10 12]

arr1 = np.array([11, 22, 33, 44, 55, 66, 77, 88, 99])
idx = np.array([0, 2, 4, 6, 8])
print(arr1[idx]) # [11 33 55 77 99]

# zeros() : 인수가 0인 ndarray 객체 생성
a1 = np.zeros((2, 2))
print(a1)
print(type(a1))
print(a1.dtype) # <class 'numpy.ndarray'>
print(a1.ndim, a1.shape) # 2 (2, 2)

# ones() : 인수가 1인 ndarray 객체 생성
a2 = np.ones((2, 3, 4), dtype = "i8")
print(a2)
print(a2.ndim, a2.shape) # 3 (2, 3, 4)

# empty(): 배열 생성만 하고 특정 값으로 초기화 안함
a4 = np.empty((3, 4))
print(a4)
print(a4.ndim, a4.shape)

# arange(): 규칙에 따라 증가하는 수열
print(np.arange(10)) # [0 1 2 3 4 5 6 7 8 9]

# full(): 사용자가 지정한 값으로 배열 생성
a5 = np.full((2, 3), 7)
print(a5)
print(a5.ndim, a5.shape)

# eye(): 대각선으로 1, 나머지는 0인 2차원 배열 생성

# 반복문을 사용하지 않고 배열의 모든 원소에 대해 하나의 명령으로 
# 반복 연산을 수행을 지원 -> vectorized operation
x = np.arange(1, 10001)
y = np.arange(10001, 20001)

z = np.zeros_like(x)
for i in range(10000):
    z[i] = x[i] + y[i]
print(z[:10])

# 이게 더 빠름
w=np.zeros_like(x)
w = x+y
print(w[:10])

# 배열 객체간의 연산: +, -, *, /, **, %, //
# 함수로 사용해도 가능: add, subtract, multiply, divide, power, mod, floor_divide
a = np.array([1, 2, 3, 4])
b = np.array([2, 4, 2, 4])
c = np.array([1, 2, 3, 4])
print((a == b)) # [False False False  True]
print((a == c)) # [ True  True  True  True]

print(np.all(a == b)) # False
print(np.all(a == c)) # True

# 벡터화 연산
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.dot(a, b))
print(np.sum(b)) # 26
print(np.sum(b, axis = 0)) # [12 14] (열별로 합계)
print(np.sum(b, axis = 1)) # [11 15] (행별로 합계)

# ndarray 객체의 크기가 서로 다른 경우에도 사칙 연산 지원
# 크기가 작은 배열 객체를 자동으로 반복 확장하여 크기가 큰 배열객체에 맞춰 사칙연산 수행
# -> broadcasting
c = np.array([1, 2, 3, 4])
d = np.array([3, 4])
print(c + 1) # [2 3 4 5]

# 2차원 과 1차원의 bradcasting 연산의 경우 행 또는 열의 원소 개수가 같아야 함
# 동일 차원의 경우 요소가 하나 이상인 경우 error


