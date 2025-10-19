# 15. Crie uma matriz 4x4 e calcule a soma de seus elementos.

import numpy as np

a = np.random.randint(0,11, size=(4,4))

print(np.sum(a))