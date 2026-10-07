import numpy as np
arr1 = np.array([10,20,30,40,50,60,70,80,90,95,85,24])
arr2 = np.array([1,22,35,44,57])
#axis = 0 : vertical stacking
#axis = 1 : horizontal stacking

new_arr = np.concatenate((arr1,arr2),axis =0)
print(new_arr)
a1=np.array([[1,2,3]])
a2=np.array([[4,5,6]])
a3=np.concatenate((a1,a2),axis=1)
print(a3)