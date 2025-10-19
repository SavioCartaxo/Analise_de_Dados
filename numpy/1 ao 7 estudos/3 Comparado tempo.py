import numpy as np
from numpy.random import default_rng
from time import process_time

rng = default_rng()

lista = list(rng.integers(10,100,1000000))

c = []
t1 = process_time() # Guarda o inicio da execução
for i in range(len(lista)):
    c.append(lista[i]*lista[i])
t2 = process_time() # Guarda o fim da execução

print(t2 - t1) # demorou 0.203125 segundos

array = rng.integers(10,100,1000000)

t1 = process_time()  # Guarda o inicio da execução
c = array * array
t2 = process_time() # Guarda o fim da execução

print(t2 - t1) # demorou 0.015625 segundos

# Conclusão: arrays são cerca de 15x mais rápidos que listas