import pandas as pd

dados = {
    'ID Funcionário': [1, 2, 3, 4, 5, 6],
    'Nome': ['Ana', 'João', 'Carlos', 'Mariana', 'Lucas', 'Fernanda'],
    'Departamento': ['TI', 'RH', 'TI', 'Vendas', 'Financeiro', 'RH'],
    'Salário': [7000, 3500, 7200, 4000, 8000, 3600],
    'Data de Admissão': ['2020-03-01', '2020-07-15', '2021-06-10', '2018-02-28', '2017-11-03', '2022-01-20'],
    'Avaliação de Desempenho': [8.5, 7.2, 9.1, 6.0, 8.0, 5.5]
}

# Tratamento inicial do df
dados_df = pd.DataFrame(dados)
dados_df['Data de Admissão'] = pd.to_datetime(dados_df['Data de Admissão'])


# Qual é o salário médio por departamento?
salario_medio_por_departamento = dados_df.groupby('Departamento')['Salário'].mean()
### dados_df = dados_df.merge(salario_medio_por_departamento, on='Departamento')


# Quem é o funcionário com a melhor avaliação?
funcionario_melhor_avaliado = dados_df.loc[dados_df['Avaliação de Desempenho'].idxmax(), 'Nome']


# Qual departamento tem o maior número de funcionários?
funcionarios = dados_df.groupby('Departamento')['Nome'].count().reset_index()
funcionarios = funcionarios.loc[funcionarios['Nome'] == funcionarios['Nome'].max(), 'Departamento']


# Qual é a média salarial dos funcionários com avaliação acima de 8?
salario_desempenho_acima_de_8 = dados_df.loc[dados_df['Avaliação de Desempenho'] > 8, 'Salário'].mean()


# Quantos funcionários foram contratados por ano?
ano = pd.DataFrame(dados_df['Data de Admissão'].dt.year)
ano = ano.rename(columns={'Data de Admissão' : 'Ano de Admissão'})
ano = ano.groupby('Ano de Admissão').size()
ano = ano.sort_values(ascending=False)


# Adicione uma nova coluna chamada Tempo de Casa(anos) com base na data de admissão.
dados_df['Tempo de Casa'] = 2025 - dados_df['Data de Admissão'].dt.year


# Crie uma análise geral agrupada por departamento
departamento_df = dados_df.groupby('Departamento')[['Salário', 'Avaliação de Desempenho']].mean()
departamento_df['Funcionários'] = dados_df.groupby('Departamento')['ID Funcionário'].nunique()
departamento_df = departamento_df.rename(columns={'Salário':'Salário Médio', 'Avaliação de Desempenho':'Desempenho médio', 'Funcionários':'N° Funcionários'})


#----------------------
#   Saídas
#----------------------

print('Qual é o salário médio por departamento?')
print(salario_medio_por_departamento, '\n')

print('Quem é o funcionário com a melhor avaliação?')
print(funcionario_melhor_avaliado,'\n')

print('Qual departamento tem o maior número de funcionários?')
print(funcionarios,'\n')

print('Qual é a média salarial dos funcionários com avaliação acima de 8?')
print(salario_desempenho_acima_de_8,'\n')

print('Quantos funcionários foram contratados por ano?')
print(ano, '\n')

print('Adicione uma nova coluna chamada Tempo de Casa(anos) com base na data de admissão.')
print(dados_df, '\n')

print('# Crie uma análise geral agrupada por departamento')
print(departamento_df)