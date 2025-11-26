# 11. Gere um array de 50 números entre 1 e 200 e encontre a média e o desvio padrão.

import numpy as np

a = np.random.randint(1, 201, size=50)

desvio = np.std(a)
media = np.mean(a)

print(media)
print(desvio)