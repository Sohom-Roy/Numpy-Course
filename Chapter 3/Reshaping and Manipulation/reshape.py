#rows*columns = len(arr)
#it doesnot creates copy
import numpy as np
arr = np.array([10,20,30,40,50,60,70,80,90,95,85,24])
arr_reshape = arr.reshape(2,2,3)
print(arr_reshape)

