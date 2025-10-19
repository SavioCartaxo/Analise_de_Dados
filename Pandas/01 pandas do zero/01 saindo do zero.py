#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas as pd

df = pd.DataFrame() # Cria um DataFrame vazio
vendas = {
    'dia' : ['15', '12', '13'],
    'valor' : [120, 100, 80],
    'produtos' : ['feijão', 'arroz', 'mandioca'],
    'quantidade' : [20, 30, 20]
    }

vendas_df = pd.DataFrame(vendas)


# In[40]:


# Formas de vizualizar
print(vendas_df) # printa no terminal

# Cria uma tabela bonitinha
display(vendas_df)
vendas_df


# In[41]:


# Lendo um arquivo do excel

vendas_df = pd.read_excel("Vendas.xlsx")
display(vendas_df)


# In[42]:


# Comaçando análise de dados

import numpy as np
import pandas as pd

display(vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping' , ['Valor Final', 'Valor Unitário', 'Quantidade']])

a = np.array([i for i in vendas_df['Quantidade']])
b = np.array([i for i in vendas_df['Valor Unitário']])

renda_total = np.sum(a * b)
print(a)
print(b)
print(a * b)

rendas_form = f'{renda_total:,}'.replace(',', '.')

print(renda_total)
print(f'{rendas_form} R$')


# In[43]:


vendas_df.head() # Mostra as primeiras 5 linhas da tabela
# Argumento do head == número de linhas a serem mostradas


# In[44]:


vendas_df.shape # Mesma coisa do numpy


# In[45]:


vendas_df.describe() # Resumo Geral para análise de dados


# In[46]:


# Mudando a forma de Vizualizar a tabela

produtos = vendas_df['Produto']
display(produtos)

# uma coluna não é um DataFrame, é uma Serie do Pandas

quero_esses = vendas_df[['Produto', 'ID Loja']]
display(quero_esses)


# In[47]:


# Filtrando Linhas e Colunas

vendas_df.loc    # A primeira parte da tabela são os indice
vendas_df.loc[1] # Primeira linha
vendas_df[1:5]   # Várias linhas de uma vez só

# Pegar linhas que correspondem a uma condição

venda_norte_shop_df = vendas_df[vendas_df["ID Loja"] == 'Norte Shopping']
venda_norte_shop_df

# Para pegar linhas e colunas:
# DataFrame[linhas, colunas]

display(vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping', ["ID Loja", "Produto", "Valor Unitário"]])


# In[48]:


# Modelo para acessar um item especifico

# DataFrame.loc[linha, coluna]

print(vendas_df.loc[93852, 'Produto']) # Produto especifico


# In[49]:


# Criando uma coluna Nova

vendas_df['Comissão'] = vendas_df['Valor Final'] * 0.05
display(vendas_df[['Valor Final', 'Comissão']])


# In[50]:


# Criando uma coluna com valor padrão
# O Pandas não gosta disso:
# vendas_df['Imposto'] = 0

# Forma correta: .loc

# vendas_df.loc[linha, coluna] = 0
# vendas_ df.loc[:, coluna] # Todas as linhas

vendas_df.loc[:, 'Impostos'] = 0
display(vendas_df)


# In[51]:


# Adicionando linhas

vendas_dez = pd.read_excel('Vendas - Dez.xlsx') # 7000 itens

vendas_df = pd.concat([vendas_df, vendas_dez], ignore_index=True)
display(vendas_df)

# pd.concat([l1, l2], ignore_index=True)


# In[52]:


# Deletando uma linha 

# vendas_df = vendas_df.drop('Impostos', axis=1) # axis 0 é a linha, 1, coluna
# vendas_df


# In[53]:


# Valores Vazios

# Deletar linhas e colunas completaente vazias
## vendas_df.dropna(how='all', axis=1) # Exclui (colunas) Vazios ##

# Se tiver pelo menos um valor vazio

## vendas_df = vendas_df.dropna() ##

# Preencher valores vazios
# Preencher com a média da coluna

## vendas_df['Comissão'] = vendas_df['Comissão'].fillna(vendas_df['Comissão'].mean()) # Preenche com a média
## display(vendas_df[['Código Venda', 'Comissão']])


# In[54]:


# Preenchendo com o último valor

## vendas_df = vendas_df.ffill()
vendas_df


# In[55]:


# Calculando Indicadores

transicoes_por_loja_df = vendas_df['ID Loja'].value_counts()
transicoes_por_loja_df


# In[56]:


# Faturamento de Cada um dos produtos

faturamento_por_produto = vendas_df[['Produto', 'Valor Unitário', 'Valor Final']].groupby('Produto')['Valor Final'].sum().reset_index()
display(faturamento_por_produto)


# In[57]:


# Procurando informações de um DF em outro

gerentes_df = pd.read_excel('Gerentes.xlsx')
vendas_df = vendas_df.merge(gerentes_df) # Como os dois têm colunas com o mesm nome, ele já mescla as duas automaticamente

display(vendas_df)


# In[58]:


analise = vendas_df.groupby('ID Loja')[['Quantidade','Valor Final','Comissão']].sum()

analise.corr()


# In[59]:


termo = pd.DataFrame(vendas_df,index=np.arange(1,100999))

termo['Comissão'] = termo['Comissão'].fillna(termo['Comissão'].mean())
termo['Impostos'] = termo['Impostos'].fillna(termo['Impostos'].mean())
display(termo)

