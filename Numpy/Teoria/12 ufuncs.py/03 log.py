# Função log
import numpy as np
from math import log

a = np.arange(1, 11)
print(np.log10(a))

nplog = np.frompyfunc(log, 2, 1)
print(nplog(4, 2)) # Logaritmo de 4 na base 2