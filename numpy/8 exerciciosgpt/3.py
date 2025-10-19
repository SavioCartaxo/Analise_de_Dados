# 3. Crie um array de 12 números aleatórios entre 1 e 100 e exiba os valores ordenados de forma decrescente.

import numpy as np

a = np.random.randint(1,101, size=12)

a = np.sort(a)

a = a[::-1]

print(a)