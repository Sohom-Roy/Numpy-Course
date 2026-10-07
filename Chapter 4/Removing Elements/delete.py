import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr)
new_arr= np.delete(arr,5)
print(new_arr)

arr2d=np.array([[1,2,3],[4,5,6]])
print(arr2d)
print(np.delete(arr2d,1,axis = 1))