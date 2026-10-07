#np.nan_to_num(array,nan=value) by default 0
import numpy as np
arr = np.array([1,2,np.nan,4,2,9,7,np.nan,10])
cleanarr=np.nan_to_num(arr,nan=1)
print(cleanarr)