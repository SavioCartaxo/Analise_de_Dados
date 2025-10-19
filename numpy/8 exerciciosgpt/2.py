# 2. Gere um array de 30 elementos entre 10 e 100 e conte quantos valores são pares.

import numpy as np

a = np.random.randint(10,101, size=30)

contador = np.sum(a % 2 == 0)

print(a)
print(contador)