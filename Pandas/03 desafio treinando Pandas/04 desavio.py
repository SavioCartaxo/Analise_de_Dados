import pandas as pd
import numpy as np

clientes_df = pd.DataFrame({
    'ID Cliente': [1, 2, 3, 4, 5], # vendas_df
    'Nome': ['Ana Paula', 'João Marcos', 'Pedro Silva', 'Mariana Lima', 'Carlos Souza'],
    'Estado': ['SP', 'RJ', 'MG', 'SP', 'BA']
})

produtos_df = pd.DataFrame({
    'ID Produto': [1, 2, 3, 4, 5], # vendas_df
    'Produto': ['Notebook', 'Camiseta', 'Celular', 'Fone de Ouvido', 'Tênis'],
    'Categoria': ['Eletrônicos', 'Roupas', 'Eletrônicos', 'Acessórios', 'Roupas'],
    'Preço Unitário': [3500, 60, 2800, 150, 300]
})

vendas_df = pd.DataFrame({
    'ID Venda': [101, 102, 103, 104, 105, 106, 107, 108],
    'ID Cliente': [1, 2, 3, 1, 4, 5, 2, 3],
    'ID Produto': [1, 2, 3, 4, 5, 2, 1, 5],
    'Quantidade': [1, 3, 1, 2, 1, 5, 1, 2],
    'Data da Venda': [
        '2024-01-10', '2024-01-12', '2024-02-05', '2024-02-20',
        '2024-03-15', '2024-03-20', '2024-04-10', '2024-04-22'
    ]
})

# Juntando os DataFrames

vendas_df = vendas_df.merge(clientes_df, on='ID Cliente')
vendas_df = vendas_df.merge(produtos_df, on='ID Produto')

# Criando total

vendas_df['Total'] = vendas_df['Quantidade'] * vendas_df['Preço Unitário']

# classificando
media = np.mean(vendas_df['Total'])
desvio = np.std(vendas_df['Total'])

vendas_df['Nivel'] = np.where(vendas_df['Total'] < media, 'Baixo',
                              np.where(vendas_df['Total'] <= (media + desvio), 'Médio', 'Alto'))

# Qual categoria teve o melhor resultado por Estado

estado = vendas_df.groupby(['Estado', 'Categoria'])['Total'].sum().reset_index() # reset_index()
estado = estado.sort_values('Total', ascending=False).groupby('Estado').first() # ascending # .first()
print(estado)

# Qual dia da semana mais teve vendas?
vendas_df['Data da Venda'] = pd.to_datetime(vendas_df['Data da Venda'])
vendas_df['Dia da semana'] = vendas_df['Data da Venda'].dt.day_name() # .dt.day_name()

dias_da_semana = vendas_df.groupby('Dia da semana')['Total'].sum()
print(f'O dia da semana que mais vendeu foi {dias_da_semana.idxmax()}')

# Crie uma análise por mês com
 # total vendido
vendas_df['Mês'] = vendas_df['Data da Venda'].dt.month_name() # dt.month
total = vendas_df.groupby('Mês')['Total'].sum()

 # número de clientes únicos
unicos = vendas_df.groupby('Mês')['ID Cliente'].nunique() # nunique - conta quantos diferentes tem

 # média de valor por cliente
media = total / unicos

analise = pd.concat([total, unicos], axis=1)
print(analise)
print(f'A média foi: \n{media}')