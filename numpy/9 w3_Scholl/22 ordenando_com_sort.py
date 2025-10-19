# Filrando elementos de um array
import numpy as np

# Primeira forma
a = np.random.randint(1,100, size=(20))
print(a[a > 40]) # seleciona apenas os maiores que 40

# Segunda forma
mascara = a > 40 # Cria uma máscara Booleana para o array
print(a[mascara])

# Terceira forma
b = np.array([], dtype='I')
for i in np.nditer(a): # Analisa cada elemento e adiciona na lista b
    if i > 40:
        b = np.append(b, i)

a = np.copy(b) # substitui a lista A pela lista filtrada(B)
print(a)