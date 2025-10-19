# parecido com o randint, mas com um "pico" no argumento p

# Três paramentros

# n - número de tentativas
# p - Pico do gráfico
# size - o formato da matriz

import numpy as np

x = np.random.binomial(n=100, p=0.50, size=1_000_000)

a = np.count_nonzero((x == 1) | (x == 0))
b = np.count_nonzero((x > 3) & (x < 7))
c = np.count_nonzero(x >= 7)

print(a, b, c)