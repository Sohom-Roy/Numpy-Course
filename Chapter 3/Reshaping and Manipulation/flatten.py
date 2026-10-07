'''
Docstring for Chapter 3.Reshaping and Manipulation.flatten
.ravel()-> view
.flatten()-> copy
'''
import numpy as np
arr = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(arr)
print(arr.ravel())
print(arr.flatten())
