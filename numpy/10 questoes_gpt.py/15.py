# 15. Encontre o índice do maior valor em um array NumPy.

import numpy as np

a = np.random.randint(10, 100, size=(5,5))

print(a)
b =np.argmax(a)

print(b)