import pandas as pd
import numpy as np

# --------------------------------------
# 1. Criando os DataFrames
# --------------------------------------

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

# --------------------------------------
# 2. Juntando as tabelas (JOIN)
# --------------------------------------

vendas_df = vendas.merge(clientes, on='ID Cliente')
vendas_df = vendas_df.merge(produtos, on='ID Produto')

# --------------------------------------
# 3. Criar coluna de valor total
# --------------------------------------

vendas_df['Total'] = vendas_df['Preço Unitário'] * vendas_df['Quantidade']
vendas_df['Data da Venda'] = pd.to_datetime(vendas_df['Data da Venda'])

# --------------------------------------
# 4. Análises principais
# --------------------------------------

# Cliente que mais comprou (em valor total)
cliente_top = vendas_df.groupby('Nome')['Total'].sum().idxmax()
valor_top = vendas_df.groupby('Nome')['Total'].sum().max()
print(f"🏆 Cliente que mais comprou: {cliente_top} (R$ {valor_top:.2f})")

# Categoria com maior faturamento
categoria_top = vendas_df.groupby('Categoria')['Total'].sum().idxmax()
faturamento_cat = vendas_df.groupby('Categoria')['Total'].sum().max()
print(f"📦 Categoria mais lucrativa: {categoria_top} (R$ {faturamento_cat:.2f})")

# Produto mais vendido em quantidade
produto_top = vendas_df.groupby('Produto')['Quantidade'].sum().idxmax()
qtd_top = vendas_df.groupby('Produto')['Quantidade'].sum().max()
print(f"📈 Produto mais vendido: {produto_top} ({qtd_top} unidades)")

# Cidade que mais gerou vendas
cidade_top = vendas_df.groupby('Cidade')['Total'].sum().idxmax()
print(f"🌆 Cidade com mais vendas: {cidade_top}")

# Dia com maior volume de vendas
dia_top = vendas_df.groupby('Data da Venda')['Total'].sum().idxmax()
valor_dia = vendas_df.groupby('Data da Venda')['Total'].sum().max()
print(f"📅 Dia com maior faturamento: {dia_top.date()} (R$ {valor_dia:.2f})")

# Média de vendas por cliente
media_cliente = vendas_df.groupby('Nome')['Total'].sum().mean()
print(f"📊 Média de vendas por cliente: R$ {media_cliente:.2f}")

# --------------------------------------
# 5. Extra: Top 3 clientes por categoria
# --------------------------------------

top3_por_categoria = vendas_df.groupby(['Categoria', 'Nome'])['Total'].sum().reset_index()
top3_por_categoria = top3_por_categoria.sort_values(['Categoria', 'Total'], ascending=[True, False])

print("\n⭐ Top 3 clientes por categoria:")
for cat in top3_por_categoria['Categoria'].unique():
    top_clientes = top3_por_categoria[top3_por_categoria['Categoria'] == cat].head(3)
    print(f"\nCategoria: {cat}")
    print(top_clientes[['Nome', 'Total']])

# --------------------------------------
# 6. Extra: Relatório de vendas por mês
# --------------------------------------

vendas_df['AnoMes'] = vendas_df['Data da Venda'].dt.to_period('M')
relatorio_mensal = vendas_df.groupby('AnoMes')['Total'].sum()

print("\n📆 Relatório de Vendas Mensal:")
print(relatorio_mensal)