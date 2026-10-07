import numpy as np
arr=np.array([1,2,50,-np.inf,658,-5874,np.inf])

print(np.isinf(arr))
cleaned_arr=np.nan_to_num(arr,posinf=10000,neginf=-10000)

print(cleaned_arr.astype(int))