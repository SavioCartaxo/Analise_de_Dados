import pandas as pd
import numpy as np

# -------------------------------
# GERAR DADOS
# -------------------------------

np.random.seed(42)

# Criar nomes dos alunos
alunos = [f'Aluno {i}' for i in range(1, 21)]

# Gerar notas aleatórias entre 0 e 10
notas = {
    'Matemática': np.random.uniform(0, 10, 20).round(1),
    'Português': np.random.uniform(0, 10, 20).round(1),
    'História': np.random.uniform(0, 10, 20).round(1),
    'Geografia': np.random.uniform(0, 10, 20).round(1),
    'Inglês': np.random.uniform(0, 10, 20).round(1)
}

# Gerar faltas aleatórias entre 0 e 15
faltas = np.random.randint(0, 16, 20)

# Criar DataFrame
df = pd.DataFrame(notas)
df['Aluno'] = alunos
df['Faltas'] = faltas
df = df[['Aluno', 'Matemática', 'Português', 'História', 'Geografia', 'Inglês', 'Faltas']]

# -------------------------------
# TRATAMENTO
# -------------------------------

# Zerar notas dos alunos com mais de 10 faltas
df.loc[df['Faltas'] > 10, ['Matemática', 'Português', 'História', 'Geografia', 'Inglês']] = 0.0

# Calcular Média Final
df['Média Final'] = df[['Matemática', 'Português', 'História', 'Geografia', 'Inglês']].mean(axis=1)

# -------------------------------
# ANÁLISES
# -------------------------------

# 1. Melhor aluno
melhor_aluno = df.loc[df['Média Final'].idxmax()]
print(f"🏆 Melhor aluno: {melhor_aluno['Aluno']} (Média: {melhor_aluno['Média Final']:.1f})")

# 2. Reprovados (média < 6 ou faltas > 10)
reprovados = df[(df['Média Final'] < 6) | (df['Faltas'] > 10)]
print(f"\n❌ Alunos reprovados: {len(reprovados)}")

# 3. Matéria com pior desempenho médio
medias_materias = df[['Matemática', 'Português', 'História', 'Geografia', 'Inglês']].mean()
pior_materia = medias_materias.idxmin()
print(f"\n📉 Pior desempenho médio: {pior_materia} ({medias_materias.min():.1f})")

# 4. Nota mais alta registrada e em qual matéria
nota_max = df[['Matemática', 'Português', 'História', 'Geografia', 'Inglês']].max().max()
materia_max = df[['Matemática', 'Português', 'História', 'Geografia', 'Inglês']].max().idxmax()
print(f"\n⭐ Nota mais alta registrada: {nota_max:.1f} ({materia_max})")