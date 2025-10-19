# 5. Crie dois arrays de 10 elementos aleatórios cada e encontre os valores que aparecem nos dois.

import numpy as np

a = np.random.randint(0, 11, size=10)
b = np.random.randint(0, 11, size=10)

c = np.intersect1d(a,b)

print(c)