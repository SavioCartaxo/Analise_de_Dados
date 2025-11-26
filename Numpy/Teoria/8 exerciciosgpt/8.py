# 8. Gere uma matriz 6x6 e encontre a posição dos valores menores que 20.

import numpy as np

a = np.random.randint(1,101, size=36)
a = a.reshape(6,6)

for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] < 20:
            print(f"({i}, {j}) == {a[i][j]}")

#pos = np.argwhere( a < 20)

print(a)
#print(pos)