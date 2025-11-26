# 12. Some todos os elementos de um array NumPy.

import numpy as np

a = np.random.randint(10, 11, size=(5,5))

#print(np.sum(a))

soma = 0

for e in np.nditer(a):
    soma += e

print(soma)