# Sorteia números float na escala escolhida(negativos e positivos)
# loc = média
# scale = desvio padrão

from numpy import random
import numpy as np

x = random.normal(size=100)

print(x)
print()

# Média e desvio padrão

x = random.normal(loc=1, scale=2, size=(2, 3))
print(x)