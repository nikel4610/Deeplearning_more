import numpy as np

# list1 = [1, 2, 3]

# print('list1 type:', type(list1))
# array1 = np.array(list1)
# #array1 = np.array([1,2,3])

# print('array1 type:',type(array1))
# print('array1 array 형태:',array1.shape)

# array2 = np.array([[1,2,3],
#                     [2,3,4]])

# print('array2 type:',type(array2))
# print('array2 array 형태:',array2.shape)

# array3 = np.array([[1,2,3]])

# print('array3 type:',type(array3))
# print('array3 array 형태:',array3.shape)

# print('array1: {:0}차원, array2: {:1}차원, array3: {:2}차원'.format(array1.ndim,array2.ndim,array3.ndim))
# ------------------------------------------------------------
# list1 = [1,2,3]

# print(type(list1))

# array1 = np.array(list1)

# print(type(array1))
# print(array1, array1.dtype)

# list2 = [1, 2, 'test']
# array2 = np.array(list2)

# print(array2, array2.dtype)

# list3 = [1, 2, 3.0]
# array3 = np.array(list3)

# print(array3, array3.dtype)

# array_int = np.array([1, 2, 3])
# array_float = array_int.astype('float64') 
# # array_int.astype(np.float64)

# print(array_float, array_float.dtype)

# array_int1= array_float.astype('int32')

# print(array_int1, array_int1.dtype)

# array_float1 = np.array([1.1, 2.1, 3.1])
# array_int2= array_float1.astype('int32')

# print(array_int2, array_int2.dtype)
# ------------------------------------------------------
# sequence_array = np.arange(10)
# print(sequence_array)
# print(sequence_array.dtype, sequence_array.shape)
# #(3, 2) shape을 가지는 모든 원소가 0, dtype은 int32 인 ndarray 생성.

# zero_array = np.zeros((3, 2), dtype='int32')
# print(zero_array)
# print(zero_array.dtype, zero_array.shape)
# #(3, 2) shape을 가지는 모든 원소가 1인 ndarray 생성. ,

# one_array = np.ones((3, 2))
# print(one_array)
# print(one_array.dtype, one_array.shape)
# ------------------------------------------------------
# array1 = np.arange(10)
# print('array1:\n', array1)
# # (2, 5) shape으로 변환

# array2 = array1.reshape(2, 5)
# print('array2:\n',array2)
# #(5, 2) shape으로 변환.

# array3 = array1.reshape(5,2)
# print('array3:\n',array3)

# # array1.reshape(4,3) # error
# array1 = np.arange(10)
# print(array1)

# array2 = array1.reshape(-1,5)
# print('array2 shape:',array2.shape)

# array3 = array1.reshape(5,-1)
# print('array3 shape:',array3.shape)

# array1 = np.arange(10)
# # array4 = array1.reshape(-1,4) # error
# array1 = np.arange(8)
# array3d = array1.reshape((2,2,2))
# print('array3d:\n',array3d.tolist())
# # 3차원 ndarray를 2차원 ndarray로 변환하되 칼럼갯수는 1

# array5 = array3d.reshape(-1, 1)
# print('array5:\n',array5.tolist())
# print('array5 shape:',array5.shape)
# # 1차원 ndarray를 2차원 ndarray로 변환화되 칼럼 갯수는 1

# array6 = array1.reshape(-1, 1)
# print('array6:\n',array6.tolist())
# print('array6 shape:',array6.shape)
# # 3차원 array를 1차원으로 변환

# array1d = array3d.reshape(-1,)
# print(array1d)
# ------------------------------------------------------
