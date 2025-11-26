# 10. Crie uma matriz 7x7 com valores aleatórios e substitua os valores negativos por 0.

import numpy as np

a = np.random.randint(-10, 11, size=(7,7))

print(a)

a[a < 0] = 0

print(a)