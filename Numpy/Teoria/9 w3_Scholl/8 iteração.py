import numpy as np

a = np.random.randint(0,101, size=(2,2,2,2))

#for d4 in a:
#    for d3 in d4:
#        for d2 in d3:
#            for d1 in d2:
#                print(d1)

# Esse método é muito ineficiente, assim é melhor:

for elemento in np.nditer(a):
    print(elemento)

# np.nditer é show papai