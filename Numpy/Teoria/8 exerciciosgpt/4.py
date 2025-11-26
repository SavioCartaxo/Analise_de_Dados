# 4. Crie um array de 10 números e troque o maior e o menor valor de posição.

import numpy as np

a = np.random.randint(1, 101, size=10)
print(a)

maior = np.argmax(a)
menor = np.argmin(a)

a[maior], a[menor] = a[menor], a[maior]

print(a)