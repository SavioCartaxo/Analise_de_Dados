# 14. Crie uma matriz 5x5 de números aleatórios e encontre o maior valor de cada linha.

import numpy as np

a = np.random.randint(0,11, size=(5,5))

print(a)

print(np.max(a, axis=1))