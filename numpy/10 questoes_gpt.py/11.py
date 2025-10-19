# 11. Extraia a diagonal principal de uma matriz 5x5 aleatória.

import numpy as np

a = np.random.randint(10,101, size=(5,5))

b = np.diagonal(a)

print(b)