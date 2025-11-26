import pandas as pd
import numpy as np

alunos = pd.DataFrame({
    'Aluno' : ['Sávio', 'Railtu', 'Xavier', 'Jefferson', 'Pedro', 'Matheus'],
    'Nota'  : [9, 10, 6, 2, 7, 4]
}, index=np.arange(1, 7))

alunos['Aprovação'] = np.where(alunos['Nota'] <  4, 'Reprovado', 
                               np.where((alunos['Nota'] >= 4) & (alunos['Nota'] < 7), 'Final', 'Aprovado'))

q_alunos = np.count_nonzero(alunos['Aluno'])
media_da_turma = np.mean(alunos['Nota'])

print(f'São {q_alunos} Alunos, com média {media_da_turma:.2f}')

n_aprovados, n_reprovados, n_final = np.count_nonzero(alunos['Aprovação'] == 'Aprovado'),np.count_nonzero(alunos['Aprovação'] == 'Reprovado'), np.count_nonzero(alunos['Aprovação'] == 'Final')
print(n_aprovados, n_reprovados, n_final)

print(np.shape(alunos)) # Numpy
print(alunos.shape)     # Pandas

print()

print(alunos[alunos['Aluno'] == 'Railtu'])

print()

maior_que_8 = alunos.loc[alunos['Nota'] >= 8, ['Aluno', 'Nota']]
print(maior_que_8)

print()
# Pegar sainda especifica

print(alunos.loc[1, 'Aluno'])

print()
# Adicionar a colúna Quanto falta para 7

alunos['Falta para Passar'] = np.where(alunos['Nota'] < 7, 7 - alunos['Nota'], None)

print(alunos)