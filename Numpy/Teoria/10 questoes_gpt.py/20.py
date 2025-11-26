# 20. Crie uma máscara booleana para encontrar os elementos maiores que 50 em um array.

import numpy as np

a = np.random.randint(0, 100, size=(5,5))

a = a > 50

b = np.count_nonzero(a == False)
c = np.count_nonzero(a == True)
print(a)

print(b)
print(c)