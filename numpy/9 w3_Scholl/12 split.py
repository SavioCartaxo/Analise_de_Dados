import numpy as np

a = np.random.randint(0, 11, size=(6,2))

a = np.array_split(a,2)

print(a)

for i in a:
    print(i)