# Tratando erros na tabela


# Empty cells - Células Vazias - None

import pandas as pd
import numpy as np

animes = pd.DataFrame({
    'Título' : ['Naruto', 'Anime'],
    'Episódios' : [None, 12] 
})

## animes = animes.dropna() # Remove vazios o que tiver pelo menos um dado vazio
## animes.dropna(inplace=True) # Faz a mesma coisa, só que sem atribuição

print(animes, '\n')

# Outra forma de fazer isso é trocando os valores vazios por valores escolhidos

animes.fillna(animes['Episódios'].mean(),inplace=True)
# .fillna com o argumento inplace
print(animes,'\n')


# Wrong data - Dados Errados
# Remover com for e if

# Duplicates - Dados duplicados

# Usamos o metodo .duplicated() 
# Retorna uma lista booleana, para remover em si, faz assim:

animes = pd.DataFrame({
    'Título' : ['Naruto', 'Anime', 'Naruto'],
    'Episódios' : [None, 12, None] 
})

animes.drop_duplicates(inplace=True)
print(animes)