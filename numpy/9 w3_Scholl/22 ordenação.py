# Ordenando um array já existente

import numpy as np

a = np.random.randint(1,101, size=100)

b = np.array([], dtype='I')
for i in np.nditer(a):
    posicao = np.searchsorted(b,i)

    b = np.insert(b,posicao,i)

a = b

print(a)