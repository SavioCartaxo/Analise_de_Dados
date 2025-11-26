import pandas as pd
import numpy as np

# -------------------------------
# GERAR DADOS SIMULADOS
# -------------------------------

np.random.seed(42)  # Para resultados reproduzíveis

# Datas
datas = pd.date_range(start='2024-01-01', periods=30)

# Produtos aleatórios
produtos = np.random.choice(['Camiseta', 'Calça', 'Tênis'], size=30)

# Quantidade aleatória entre 1 e 10
quantidades = np.random.randint(1, 11, size=30)

# Preço por produto
precos = {'Camiseta': 50, 'Calça': 100, 'Tênis': 200}
preco_unitario = [precos[produto] for produto in produtos]

# ID de loja aleatório
lojas = np.random.choice(['Loja A', 'Loja B', 'Loja C'], size=30)

# Criar DataFrame
vendas = pd.DataFrame({
    'Data': datas,
    'Produto': produtos,
    'Quantidade': quantidades,
    'Preço Unitário': preco_unitario,
    'ID Loja': lojas
})

# Criar coluna Valor Total
vendas['Valor Total'] = vendas['Quantidade'] * vendas['Preço Unitário']

# -------------------------------
# ANÁLISES
# -------------------------------

# 1. Produto mais vendido (em quantidade)
agrupado_produtos = vendas.groupby('Produto')[['Quantidade', 'Valor Total']].sum()
produto_top = agrupado_produtos['Quantidade'].idxmax()
quantidade_top = agrupado_produtos['Quantidade'].max()
print(f'Produto mais vendido: {produto_top} ({quantidade_top} unidades)')

# 2. Faturamento total da loja (por loja)
faturamento_lojas = vendas.groupby('ID Loja')['Valor Total'].sum()
print('\nFaturamento total por loja:')
print(faturamento_lojas.sort_values(ascending=False))

# 3. Dia com maior faturamento
faturamento_dias = vendas.groupby('Data')['Valor Total'].sum()
dia_top = faturamento_dias.idxmax()
valor_dia_top = faturamento_dias.max()
print(f'\nDia com maior faturamento: {dia_top.date()} (R$ {valor_dia_top:.2f})')

# 4. Valor médio vendido por dia
media_diaria = faturamento_dias.mean()
print(f'\nValor médio vendido por dia: R$ {media_diaria:.2f}')