# 13. Gere dois arrays aleatórios de tamanho 10 e calcule o produto escalar entre eles.

import numpy as np

a = np.random.randint(0,11, size=10)
b = np.random.randint(0,11, size=10)

print(np.sum(a*b))