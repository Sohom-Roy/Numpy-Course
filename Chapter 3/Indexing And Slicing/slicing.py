import numpy as np
arr =np.array([10,20,30,40,50,60,70,80,90])
#[start:end-1:step]
print(arr[1:10:2])

#print complete list
print(arr[0:9])
print(arr[:])
print(arr[::])
print(arr[0:len(arr)])

#print reverse list
print(arr[::-1])