import numpy as np
arr1 = np.array([[1,2,3],[4,5,6]])#shape(2,3)
arr2 = np.array([7,8])#shape(1,2)
result=[]
result = arr1+arr2
print(result)
'''
Error:
    result = arr1+arr2
             ~~~~^~~~~
ValueError: operands could not be broadcast together with shapes (2,3) (2,)

'''