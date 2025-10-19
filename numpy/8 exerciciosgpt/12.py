# 12. Crie um array de 20 números e normalize os valores entre 0 e 1.

import numpy as np

a = np.random.randint(1, 11, size=20)

a = (a - np.min(a)) /(np.max(a) - np.min(a))

print(a)