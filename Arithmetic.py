import numpy as np
#Scalar Operations
'''array=np.array([1,2,3])
print(array+1)
print(array-1)
print(array*2)
#vector Operations
array2=np.array([4,5,6])
print(np.sqrt(array2))
array3=np.array([1.43,2.56,3.78])
print(np.round(array3))'''
#element wise operations
array1=np.array([1,2,3])
array2=np.array([4,5,6])
print(array1+array2)
print(array1-array2)    
print(array1*array2)    
print(array1/array2)
print(array1**array2)
#comparison operations
scores=np.array([78, 90, 45, 23, 67])
print(scores>50)
print(scores<=67)
scores[scores>50]=0
print(scores)