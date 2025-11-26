import pandas as pd
import numpy as np


# Criando DataFrames
clientes = pd.DataFrame({
    'ID Cliente': [1, 2],
    'Nome': ['Ana Paula', 'João Marcos'],
    'Cidade': ['São Paulo', 'Rio de Janeiro']
})

produtos = pd.DataFrame({
    'ID Produto': [1, 2, 3],
    'Produto': ['Camiseta', 'Notebook', 'Fone de Ouvido'],
    'Categoria': ['Roupas', 'Eletrônicos', 'Eletrônicos'],
    'Preço Unitário': [50, 3500, 150]
})

vendas = pd.DataFrame({
    'ID Venda': [1, 2, 3, 4],
    'ID Cliente': [1, 2, 1, 2],
    'ID Produto': [2, 1, 3, 2],
    'Quantidade': [1, 2, 3, 1],
    'Data da Venda': ['2024-02-01', '2024-02-01', '2024-03-05', '2024-03-10']
})

# Juntando DataFramesy
vendas_df = clientes.merge(vendas, on='ID Cliente')
vendas_df = vendas_df.merge(produtos, on='ID Produto')

# Valor Total
vendas_df['Total'] = vendas_df['Preço Unitário'] * vendas_df['Quantidade']

#✅ O cliente que mais comprou em valor total.
mais_vendeu = vendas_df['Total'].idxmax()
mais_vendeu = vendas_df.loc[mais_vendeu, 'Nome']
valor = vendas_df['Total'].max()

print(f'O que mais comprou foi {mais_vendeu}: {valor} R$\n')

#✅ A categoria com maior faturamento.
categorias = vendas_df.groupby('Categoria')['Total'].sum() # uma séries do Pandas, não um df
mair_faturamento = categorias.idxmax()
faturamento = categorias.max()
print(f'maior faturamento foi o de {mair_faturamento}, que faturo {faturamento}\n')

#✅ O produto mais vendido (em quantidade).
produtos = vendas_df.groupby('Produto')['Quantidade'].sum()
print(f'O produto mais vendido foi {produtos.idxmax()}, que vendeu {produtos.max()} unidades\n')

#✅ A cidade que mais gerou vendas (em valor total).
cidade = vendas_df.groupby('Cidade')['Total'].sum()
print(f'A cidade que mais fez vendas foi {cidade.idxmax()}, que vendeu {cidade.max()}\n')

#✅ O dia com maior volume de vendas.
dias = vendas_df.groupby('Data da Venda')['Total'].sum()
print(f'O dia com mais vendas foi o dia {dias.idxmax()}, com {dias.max()} vendas\n')

#✅ A média de vendas por cliente.
clientes = vendas_df.groupby('Nome')['Total'].sum()
print(f'A média de vendas por cliente é {clientes.mean()} R$')

print(vendas_df)