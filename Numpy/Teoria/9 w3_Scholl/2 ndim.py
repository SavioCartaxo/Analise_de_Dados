# Para saber quantas dimensões matriz.ndim
# Para dizer o número de dimensões, usamos ndmin no np.array
import numpy as np

a = np.array([[1,2,3],[1,2,3]], ndmin=5)

print(a)
print(a.ndim)