import numpy as np

a = np.random.randint(1, 101, size=(15,2))

a = a.reshape((6,-1))

a = a > 30

print(a)