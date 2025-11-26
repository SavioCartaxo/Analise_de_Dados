import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view() # a.view cria uma outra chamada para o mesmo array
arr[0] = 42

print(arr)
print(x)