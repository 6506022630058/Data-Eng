import numpy as np

arr = np.empty((6,4))
for i in range(6):
    arr[i] = i
print(arr)
print(arr[[3,2,5]]) # row 3 , row 2 , row 5

arr1 = np.arange(24).reshape((6,4))
print(arr1)
print(arr1[[3,2,5],[2,0,1]])  # (row, column)  ->  (3,2) , (2,0) , (5,1)

# axis 0 : row , axis 1 : column