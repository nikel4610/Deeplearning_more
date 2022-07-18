import numpy as np

list1 = [1, 2, 3]

print('list1 type:', type(list1))
array1 = np.array(list1)
#array1 = np.array([1,2,3])

print('array1 type:',type(array1))
print('array1 array 형태:',array1.shape)

array2 = np.array([[1,2,3],
                    [2,3,4]])

print('array2 type:',type(array2))
print('array2 array 형태:',array2.shape)

array3 = np.array([[1,2,3]])

print('array3 type:',type(array3))
print('array3 array 형태:',array3.shape)

print('array1: {:0}차원, array2: {:1}차원, array3: {:2}차원'.format(array1.ndim,array2.ndim,array3.ndim))
