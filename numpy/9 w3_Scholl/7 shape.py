import numpy as np

a = np.random.randint(1, 101, size=27)

a = a.reshape(3,3-1) # O -1 completa a dimensão com o que faltar

print(a)