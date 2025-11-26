# Escolhe números aleatórios em um array ou lista

import numpy as np

a = np.random.choice(b := np.array([1,2,3,4,5,6,7,8,9,0]), size=3)

print(a)

# Adicionando probabilidade no sorteio

pokemons = np.array([1, 2, 3, 4, 5])
sorteio = np.random.choice(pokemons, p=[0.5, 0.25, 0.125, 0.1, 0.025], size=1000)

print(sorteio)

# Conta o número de elementos nessa atriz ai

c1 = np.count_nonzero(sorteio == 1)
c2 = np.count_nonzero(sorteio == 2)
c3 = np.count_nonzero(sorteio == 3)
c4 = np.count_nonzero(sorteio == 4)
c5 = np.count_nonzero(sorteio == 5)

print(c1,c2,c3,c4,c5)