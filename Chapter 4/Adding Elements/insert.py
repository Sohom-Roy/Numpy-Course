#np.insert(array,indes,value,axix = None)
import numpy as np
arr = np.array([10,20,30,40,50,60,70,80,90,95,85,24])
print(arr)
new_arr=np.insert(arr,2,100)
print(new_arr)