import numpy as np

#with lists
list=[10,20,30,40,50,60]
print(list)
arr1=np.array(list)
print(arr1)

#fill with zeros
arr2 = np.zeros(3)
print(arr2)

#fill with once
arr3 = np.ones((3,3))
print(arr3)

#fill with specific value
arr4 = np.full((2,3),21)
print(arr4)

#fill with sequence of numbers
arr5 = np.arange(1,50,4)
print(arr5)

#identity matrix
arr6 = np.eye(4)
print(arr6)
