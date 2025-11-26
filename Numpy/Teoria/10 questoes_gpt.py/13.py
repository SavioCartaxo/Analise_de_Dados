# 13. Encontre o maior e o menor valor de um array NumPy.

import numpy as np

a = np.random.randint(10, 100, size=(25,5))

print( np.max(a) )
print( np.min(a) )