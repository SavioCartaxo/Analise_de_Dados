import pandas as pd

animes = {
    'Título' : ['Sasaki to Pii-chan', 'Bocchi the Rock', 'Dandadan', 'Fuguushoku "Kanteishi" ga Jitsu wa Saikyou Datta', 'Jigokurku'],
    'Notas'  : [ None , 8, 9, 7, 8],
    'Episódios' : [12, 12, 12, 12, 13] 
     }

animes_df = pd.DataFrame(animes, index= [f'Anime {i}' for i in range(1,6)])

print(animes_df,'\n')
print(animes_df['Título'].loc['Anime 3'])