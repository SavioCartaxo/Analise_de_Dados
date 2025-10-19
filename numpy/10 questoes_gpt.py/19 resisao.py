import numpy as np

a = np.arange(1,101)

a = np.array_split(a, 2)

#print(a)

a = np.random.randint(1,101, size=(5,5))
print(a)
print(a[1:4, 1:4])