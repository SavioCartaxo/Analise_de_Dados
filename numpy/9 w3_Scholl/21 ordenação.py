# Ordenando um array aleatório

import numpy as np

b = np.array([], dtype='I')
for c in range(100):
    a = np.random.randint(0,1001)

    i = np.searchsorted(b, a)

    b = np.insert(b, i, a)
print(b)