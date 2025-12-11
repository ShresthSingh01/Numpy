import numpy as np
#random number generation
rng=np.random.default_rng()
random_integers=rng.integers(low=1, high=100, size=(2,3))
print("Random Integers:", random_integers)
rang=np.random.default_rng(seed=1)  #setting seed for reproducibility
random_floats=rang.random(size=(2,3))
print("Random Floats:", random_floats)
#shuf`fling an array
array=np.array([1,2,3,4,5,6,7,8,9,10])
rng.shuffle(array)
print("Shuffled Array:", array)
fruits=np.array(['apple','banana','cherry','date','elderberry'])
rng.shuffle(fruits)
print("Shuffled Fruits:", fruits)
fruits=rng.choice(fruits, size=3)
print("Randomly Selected Fruits:", fruits)
