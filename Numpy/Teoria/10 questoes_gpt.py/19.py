# 19. Substitua todos os valores menores que 10 em um array por 0.

import numpy as np

a = np.random.randint(0, 21, size=(5,5))

a[a<10] = 0

print(a)