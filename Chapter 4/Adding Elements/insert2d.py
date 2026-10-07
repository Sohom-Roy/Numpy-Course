import numpy as np
arr = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(arr)
new_arr_row = np.insert(arr,1,[4,5,6],axis=0)
print(new_arr_row)
new_arr_col = np.insert(arr,1,[52,25,61],axis=1)
print(new_arr_col)