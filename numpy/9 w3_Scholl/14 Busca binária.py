# localiza onde indexar o número no meio da lista, usa busca binária para procurar a posição
# Retorna o indice que deve ser inserido
# Busca organizada

import numpy as np

a = np.linspace(0, 5000, endpoint=True, num=1001, dtype="I")

print(a)

x = np.searchsorted(a, 5000)

print(x)