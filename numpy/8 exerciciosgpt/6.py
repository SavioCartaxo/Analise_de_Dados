# 6. Crie uma matriz 5x5 com números de 1 a 25 e inverta as linhas e colunas (transposta).

import numpy as np

a = np.random.randint(1,26, size=(6,5))
print(a)
print(a.shape[0])
print(a.shape[1])