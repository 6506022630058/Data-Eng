import numpy as np

arr = np.array([[1,2,3],[4,5,6,]])
print(arr)
c_arr = arr.copy()
print(c_arr)

print(c_arr[1,:])
arr[1,:]=99
print(arr)
arr[:,2] = 77
print(arr)
print(arr[:2,1:])

print('-------------------------------------------')
arr2 = np.arange(1,11)
arr3 = arr2 > 7
print(arr3)