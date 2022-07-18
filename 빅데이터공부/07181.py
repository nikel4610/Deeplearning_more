import numpy as np

# 1에서 부터 9 까지의 1차원 ndarray 생성
# array1 = np.arange(start=1, stop=10)
# print('array1:',array1)
# # index는 0 부터 시작하므로 array1[2]는 3번째 index 위치의 데이터 값을 의미

# value = array1[2]
# print('value:',value)
# print(type(value))
# print('맨 뒤의 값:',array1[-1], ', 맨 뒤에서 두번째 값:',array1[-2])

# array1[0] = 9
# array1[8] = 0
# print('array1:',array1)

# array1d = np.arange(start=1, stop=10)
# array2d = array1d.reshape(3,3)
# print(array2d)
# print('(row=0,col=0) index 가리키는 값:', array2d[0,0] )
# print('(row=0,col=1) index 가리키는 값:', array2d[0,1] )
# print('(row=1,col=0) index 가리키는 값:', array2d[1,0] )
# print('(row=2,col=2) index 가리키는 값:', array2d[2,2] )
# ------------------------------------------------------
# 팬시 인덱싱
array1d = np.arange(start=1, stop=10)
array2d = array1d.reshape(3,3)
print(array2d)
array3 = array2d[[0,1], 2]
print('array2d[[0,1], 2] => ',array3.tolist())
array4 = array2d[[0,1], 0:2]
print('array2d[[0,1], 0:2] => ',array4.tolist())
array5 = array2d[[0,1]]
print('array2d[[0,1]] => ',array5.tolist())
# ------------------------------------------------------
