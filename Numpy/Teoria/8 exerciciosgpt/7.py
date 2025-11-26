# 7. Crie uma matriz 4x4 e substitua todos os valores da diagonal principal por 100.

import numpy as np

a = np.zeros((4,4), dtype=int)

#np.fill_diagonal(a, 100)

for i in range(len(a)):
    a[i,i] = 100


print(a)