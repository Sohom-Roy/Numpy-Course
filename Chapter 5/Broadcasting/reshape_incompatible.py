import numpy as np

arr1 = np.array([[1,2,3],[4,5,6]])  # shape (2,3)
arr2 = np.array([7,8])              # shape (2,)

arr2 = arr2.reshape(2,1)            # reshape to (2,1)

result = arr1 + arr2
print(result)
'''
arr2 becomes:
[[7]
 [8]]

Broadcasted to:
[[7 7 7]
 [8 8 8]]

'''