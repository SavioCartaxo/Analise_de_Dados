import numpy as np

a = np.random.randint(0,101, size=25)
b = np.random.randint(0,101, size=25)
c = np.concatenate((a,b))
print(a)
print(b)
print(c)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1) # axis=1 pega a dimensão 1(geralmente, cada linha da matriz)

print(arr)