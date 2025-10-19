import pandas as pd
import numpy as np

notas_df = pd.DataFrame({
    'Aluno': ['Ana', 'João', 'Carlos', 'Ana', 'João', 'Carlos', 'Ana', 'João', 'Carlos'],
    'Disciplina': ['Matemática', 'Matemática', 'Matemática',
                   'História', 'História', 'História',
                   'Biologia', 'Biologia', 'Biologia'],
    'Nota': [8.5, 6.0, 7.0, 9.0, 5.5, 6.0, 7.5, 6.5, 6.5]
})

# Organizando o df
notas_df = notas_df.pivot(index='Aluno', columns='Disciplina', values='Nota') # Estudar esse método

# Calculano Média
notas_df['Média'] = notas_df[['Matemática', 'História', 'Biologia']].mean(axis=1).round(1) # Round e esse axis

# Aprovado reprovado
notas_df['Aprovação'] = np.where(notas_df['Média'] >= 7, 'Aprovado',
                                 np.where(notas_df['Média'] < 5, 'Reprovado', 'Recuperação'))

# Média geral de cada disciplina
media = notas_df[['Matemática', 'História', 'Biologia']].mean().round(1)
notas_df.loc['Média Da Turma'] =  media

# Descubra qual aluno teve a melhor média geral.
aluno = notas_df['Média'].idxmax()

# Mostre um ranking dos alunos (do melhor para o pior).
aluno = notas_df.sort_values(by='Média', ascending=False) #######


print(notas_df)