import pandas as pd
import numpy as np

alunos = np.array([f'Aluno {i}' for i in range(1,21)])
materias = ['Matemática', 'Português', 'História', 'Geografia', 'Inglês']
notas = np.round(np.random.rand(20,5) * 10, 1)
faltas = np.random.randint(0, 13, size=20)

notas_df = pd.DataFrame(notas, columns=materias)
alunos_df = pd.DataFrame({
    'Alunos'   : alunos,
    'Faltas'   : faltas,
})

df = pd.concat([alunos_df, notas_df], axis=1)
df = df.set_index('Alunos')

medias = []
for i in range(20):
    media = df.loc[df.index[i], ['Matemática', 'Português', 'História', 'Geografia', 'Inglês']].mean()
    media = media.round(1)
    medias.append(media)

df['Média'] = medias

df['Aprovação'] = np.where((df['Faltas'] >= 10) | (df['Média'] < 5), 'Reprovação', 'Passou')

print(df)

# Qual foi o melhor aluno da turma?
am = df['Média'].idxmax()
print(f'Maior nota: {am}')

# Quantos alunos foram reprovados? 
ar = np.count_nonzero(df['Aprovação'] == 'Reprovação')
print(f'Reprovados: {ar}')

# Qual foi a matéria com pior desempenho médio?

menor = 11
i_menor = 0
for i in materias:
    if df[i].mean() < menor:
        menor = np.round(df[i].mean(), 1)
        i_menor = i

print(f'A matéria com a pior nota foi {i_menor}, com {menor} de média')

# Qual foi a nota mais alta registrada e em qual matéria?

maior = 0
for materia in materias:
    for i in df[materia]:
        if i > maior:
            maior = i
            maior_materia = materia

print(f'A maior nota foi {maior}, na matéria {maior_materia}')


# Estudar o .index
# Reassistir aula do 0 Pandas
# revisar todas as páginas de estudos