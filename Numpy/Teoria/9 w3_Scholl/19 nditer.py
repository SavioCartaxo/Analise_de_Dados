import numpy as np 

a = np.random.randint(1,101, size=(2,2,2))
print(a)
for i in np.nditer(a):
    print(i)

 
print()


arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)