import numpy as np
arr=np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])
x=np.sin(arr)
y=np.cos(arr)
print("Sine values:", x)
print("Cosine values:", y) 
#converting radians to degrees
degrees=np.degrees(arr)
print("Degrees:", degrees)  