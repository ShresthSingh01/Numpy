import numpy as np
array=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
#array[start:stop:step , start:stop:step]
print(array[2])
print(array[-2])
print(array[0:3])
print(array[0:3:2])
#for accessing columns
print(array[:,2])
print(array[:,1:3])
#first 3 columns
print(array[:,0:3])
