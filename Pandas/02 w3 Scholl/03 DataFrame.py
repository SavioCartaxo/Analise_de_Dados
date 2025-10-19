# Uma Serie ocorre quano há 1 dimensão
# Um data Frame ocorre em 2 dimensões: linhas e colunas(é uma matriz)

import pandas as pd

animes = pd.DataFrame({
    'Título' : ['Sasaki to Pii-chan', 'Bocchi the Rock', 'Dandadan', 'Fuguushoku "Kanteishi" ga Jitsu wa Saikyou Datta', 'Jigokurku'],
    'Notas'  : [ None , 8, 9, 7, 8],
    'Episódios' : [12, 12, 12, 12, 13] 
     })

print(animes.loc[0])

# O .loc acessa a coluna do DF como uma linha

# Saida:

# Título       Sasaki to Pii-chan
# Notas                       NaN
# Episódios                    12

# Para acessar vários ao mesmo tempo:

print(animes.loc[2:4])