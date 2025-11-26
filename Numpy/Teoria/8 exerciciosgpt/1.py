# 1. Crie um array de 15 números aleatórios entre 1 e 50 e substitua todos os múltiplos de 5 por -1.

import numpy as np

a = np.random.randint(1,51, size=15)

print(a)
a[a % 5 == 0] = -1
print(a)