import numpy as np

data = np.random.uniform(1,10,(2,4))
print(data)
print(data.shape) # (row,column)
print(data.size)  # num of elements
print(data.ravel())
print("-------------------------------------------")
data2 = data.reshape(4,2)
print(data2)
print(data2[0][1])
print(data2[1,:])
print(data2[:,1])
# data3 = data.reshape(3,3)
# print(data3)
