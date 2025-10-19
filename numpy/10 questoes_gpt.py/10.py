# 10. Redimensione um array de tamanho 9 para uma matriz 3x3.

import numpy as np

a = np.random.randint(10,101, size=9)

a = a.reshape((3,3))

print(a)