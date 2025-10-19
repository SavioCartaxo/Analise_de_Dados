#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np

vendas = pd.read_excel('Vendas.xlsx')
display(vendas.head())


# In[26]:


vendas['Valor Total'] = vendas['Quantidade'] * vendas['Valor Unitário']
#vendas.drop('Valor Final', axis=1, inplace=True)
display(vendas.head())


# In[74]:


# Análise
# Para organizar crescente
# .sort_values(by='Valor Total')

# mais_vendido

mais_vendido = vendas.groupby('Produto')[['Valor Total', 'Quantidade']].sum()

produto_mais_vendido = mais_vendido['Quantidade'].idxmax()

##print(f'O produto mais vendido foi: {produto_mais_vendido}')
##print(f'{produto_mais_vendido} Vendeu {mais_vendido['Quantidade'].max()} Itens')

# Qual foi o faturamento total da loja?
lojas = vendas.groupby('ID Loja')['Valor Total'].sum()
##print(lojas.sort_values())
##print(lojas.idxmax())

# Qual foi o dia com maior faturamento?
vendas
data = vendas.groupby('Data')['Valor Total'].sum()
print(data.sort_values())
print(data.idxmax())

# Qual foi o valor médio vendido por dia?
media = data.mean()
print(media)

