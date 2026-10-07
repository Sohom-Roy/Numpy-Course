import numpy as np
arr1 = np.array([[1,2,3],[4,5,6]])#(2,3)
arr2 = np.array([7,8,9])#(3,0)
arr3 = np.array([[7,8,9]])#(1,3)
arr4 = np.array([[1,2,3],[4,5,6],[7,8,9]])#(3,3)
print(arr1.shape)
print(arr2.shape)
print(arr3.shape)
print(arr4.shape)

result1 = arr1+arr2
result2 = arr1+arr3
#result3 = arr1+arr4
result4 = arr4+arr2
print(result1)
print(result2)
#print(result3)
print(result4)
'''
[[1+7,2+8,3+9
4+7,5+8,6+9]]

result1 = result2 
 [[  8 10 12  ]
 [  11 13 15 ]]

result3 = arr1+arr4
              ~~~~^~~~~
ValueError: operands could not be broadcast together with shapes (2,3) (3,3)

result4=
[[ 8 10 12]
 [11 13 15]
 [14 16 18]]
'''