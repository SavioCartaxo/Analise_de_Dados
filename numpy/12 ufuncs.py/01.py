# Algumas funções ufunc esseciais de numpy

import numpy as np
from numpy import random

a = random.randint(10, size=10)
b = random.randint(10, size=10)


# Somar elementos de uma matriz com as e outra
c = np.add(a,b)
# Mesma coisa de a + b

# Subtradir elementos de uma matriz com as e outra
c = np.subtract(a,b)
# Mesma coisa de a - b

np.multiply(a,b)
np.divide(a,b)
np.power(a,b)
np.mod(a,b) # a % b
np.divmod(a,b) # retorna 2 arrays, um com o quociente, outro com o mod(resto)
np.absolute(a) # abs(a)
print(a)
print(b)
print(abs(a))