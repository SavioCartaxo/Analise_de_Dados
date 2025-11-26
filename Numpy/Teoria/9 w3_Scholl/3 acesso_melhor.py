# Tem um jeito melhor de acesar os elementos de uma matriz

import numpy as np

a = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print(a[1,2]) # esse jeito é bem melhor
print(a[:,2]) # isso aqui é bom saber também