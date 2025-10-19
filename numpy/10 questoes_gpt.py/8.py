# 8. Gere um array aleatório de inteiros entre 10 e 100 com tamanho 5x5.

import numpy as np

a = np.random.randint(10,101, size=(5,5))

print(a)