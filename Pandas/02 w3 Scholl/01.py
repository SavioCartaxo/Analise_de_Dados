import pandas as pd
import numpy as np

animes = {
    'Título' : ['Sasaki to Pii-chan', 'Bocchi the Rock', 'Dandadan', 'Fuguushoku "Kanteishi" ga Jitsu wa Saikyou Datta', 'Jigokurku'],
    'Notas'  : [ None , 8, 9, 7, 8],
    'Episódios' : [12, 12, 12, 12, 13]
}

animes_df = pd.DataFrame(animes)

print(animes_df)

print(f'A média das notas dos animes é: {(np.mean(animes_df['Notas'])):.2f}')
print(f'A média de episódios dos animes é: {(np.mean(animes_df['Episódios'])):.2f}')