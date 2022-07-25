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

# min, max, sum, mean, median, std, var: 연산 수행 후 차원이 축소됨
# 2차운 이상의 ndarray객체에 axis = 0, axis = 1 적용 가능
# argmin, argmax: ndarray 객체의 원소 중 최솟값, 최댓값이 저장된 위치 반환
b = np.array([[5, 6], [7, 8]])
print(np.min(b)) # 5
print(np.max(b)) # 8
print(b.argmin()) # 0
print(b.argmax()) # 3

# ndarray 객체의 원소 자료형 dtype: b, i8, u8, c16, O, S, U
b = np.array([[5, 6], [7, 8]])
# b에 저장된 ndarray 객체의 전치 연산(transpose)
print(b.T)

# ndarray 객체의 차원의 크기 변경
# reshape, flatten, newaxis
a = np.arange(12)
b = a.reshape(3, 4)
print(b)
c = a.reshape(4, -1) # -1은 자동으로 차원의 크기를 계산
print(c)
d = a.reshape(2, 2, -1) # 2층 구조로 변경
print(d)

print(c.flatten()) # 1차원 배열로 변환

# newaxis: 차원만 1차원 증가시킴
q = np.arange(5)[:, np.newaxis] # 열로 변환
print(q)

# ndarray 연결시켜주는 함수
# hstack: 행 수가 동일한 두 ndarray 객체를 연결
# vstack: 열 수가 동일한 두 ndarray 객체를 연결
a1 = np.ones((2, 3))
a2 = np.zeros((2, 2))
print(np.hstack((a1, a2)))

b1 = np.ones((2, 3))
b2 = np.zeros((1, 3))
print(np.vstack((b1, b2)))

# dstack: 깊이 방향으로 ndarray객체를 연결
c1 = np.ones((2, 3))
c2 = np.zeros((2, 3))
print(np.dstack((c1, c2)))
print(np.dstack((c1, c2)).shape) # (2, 3, 2)

# stack: 그냥 차원을 쌓는다
print(np.stack((c1, c2)))
# [[[1. 1. 1.]
#   [1. 1. 1.]]

#  [[0. 0. 0.]
#   [0. 0. 0.]]]
print(np.stack((c1, c2)).shape) # (2, 2, 3)

print(np.stack((c1, c2), axis = 1))
# [[[1. 1. 1.]
#   [0. 0. 0.]]

#  [[1. 1. 1.]
#   [0. 0. 0.]]]
print(np.stack((c1, c2), axis = 1).shape) # (2, 2, 3)

# 사분위수 반환 함수: percentile(ndarray, 0) 최솟값
#                   percentile(ndarray, 25) 1사분위
#                   percentile(ndarray, 50) 2사분위(중앙값)
#                   percentile(ndarray, 75) 3사분위
#                   percentile(ndarray, 100) 최댓값

# 난수 생성 함수
# seed: 난수 생성을 위한 값 
# rand: 0~1 사이의 난수 생성
np.random.seed(0) 
print(np.random.rand(5)) # 5개의 난수 생성

# shuffle(): 데이터의 순서를 바꾸는 함수
# choice(ndarrat객체, size = None, replace = True, p = None): 샘플링(무작위 선택)
# randn: 정규분포를 따르는 난수 생성
# randint: 균일분포의 정수 난수 생성
# unique(, return_counts): ndarray객체의 원소중에서 중복된 값을 제외하고 중복되지 않는 값을 리스트로 반환 
print(np.unique([1, 2, 1, 3, 1, 4, 1, 5])) # [1 2 3 4 5]
print(np.unique([1, 2, 1, 3, 1, 4, 1, 5], return_counts = True)) # (array([1, 2, 3, 4, 5]), array([4, 1, 1, 1, 1], dtype=int64))

# bincount(): 0부터 minlength - 1 까지의 숫자에서 각각 값의 개수를 카운트
print(np.bincount([1, 2, 1, 3, 1, 4, 1, 5], minlength = 6)) # [0 4 1 1 1 1]

# 정수 부분만 추출하기
np.random.seed(0)
z = np.random.uniform(0, 10, 10)
print(z//1) 

# 행의 값이 0 ~ 4 정수 데이터로 구성된 5x5 2차원 배열 생성
a = np.zeros((5, 5))
a += np.arange(5)
print(a)

# random()함수로 10개의 원소를 생성하고, 생성된 원소중 최대값을 0으로 변경
a = np.random.random(10)
a[a.argmax()] = 0
print(a)

# 크기가 10인 램덤 벡터 생성하고 오름차순으로 정렬
t = np.random.random(10)
t.sort()
print(t)

# 빈도수가 가장 높은 값을 출력
z = np.random.randint(0, 10, 50)
print(np.argmax(np.bincount(z)))

