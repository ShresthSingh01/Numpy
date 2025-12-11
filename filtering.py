import numpy as np
ages=np.array([22, 25, 30, 35, 40, 45, 50, 55, 60, 65])
#filtering operations
teens=ages[ages>20]
print("Teens:", teens)
adults=ages[(ages>=30) & (ages<=50)]
print("Adults:", adults)
evens=ages[ages%2==0]
print("Even ages:", evens)
odds=ages[ages%2!=0]
print("Odd ages:", odds)
#usingnp.where
young_or_old=np.where(ages<40, 'Young', 'Old')
print("Young or Old:", young_or_old)