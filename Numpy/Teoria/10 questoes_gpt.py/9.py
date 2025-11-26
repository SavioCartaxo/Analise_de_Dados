# 9. Obtenha o shape de um array NumPy (quantidade de linhas e colunas).

import numpy as np

a = np.random.randint(10,101, size=(5,5))

print(np.shape(a))