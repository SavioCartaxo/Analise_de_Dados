import numpy as np

a = np.random.randint(1,101, size=(5,5))

meio = len(a[0]) // 2
a[:,meio] = 0 

print(a)