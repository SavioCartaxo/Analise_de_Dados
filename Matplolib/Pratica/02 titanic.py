#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('titanic')


# In[2]:


df = df.drop(['sibsp', 'parch', 'adult_male', 'deck'], axis=1)
df


# In[3]:


df.describe().round(1)


# In[4]:


df.info()


# In[5]:


# fazer um gráfico de analise dos 3 pontos de embarque e ver quantos sobreviveram em cada um


# In[6]:


# Completando espaços vazios com a idade média

df['age'] = (df['age'].fillna(df['age'].mean())).astype(int)
df


# In[7]:


# Análises simples com pandas

# Taxa de sobrevivência: calcule a média da coluna survived
media_sobreviventes = (df['survived'].mean() * 100).round(1)
print("Taxa de sobrevivência: ",media_sobreviventes, "%")

# Número total de sobreviventes por sexo
agrup_sexo = df.groupby('sex')['survived'].sum()
print(f'sobreviventes Homens: {agrup_sexo['male']}')
print(f'sobreviventes Mulheres: {agrup_sexo['female']}')

# Média de idade dos sobreviventes vs não sobreviventes
sobreviventes = df.groupby('survived')['age'].mean().round(1)
print(f"Média da idade dos sobreviventes: {sobreviventes[1]}")
print(f"Média da idade dos não sobreviventes: {sobreviventes[0]}")


# In[8]:


# Gráficos com matplotlib.pyplot

# Barras: número de passageiros por classe (pclass)
passageiros_por_classe = df['pclass'].value_counts()

x = passageiros_por_classe.index
y = passageiros_por_classe.values

plt.bar(x, y, color='k')
plt.title('Sobreviventes por classe', loc='left')
plt.xlabel("Classes")
plt.ylabel("Número de sobreviventes")
plt.show()


# In[20]:


# Pizza: proporção de sobreviventes vs não sobreviventes
sobreviventes_e_nao_sobreviventes = df['survived'].value_counts()

x = sobreviventes_e_nao_sobreviventes.values
nomes = np.array(['Mortos', 'Vivos'])
cores = np.array(['Red', 'Blue'])

plt.pie(x, labels=nomes, colors=cores)
plt.title("Sobreviventes x mortos")
plt.show()


# In[28]:


# Histograma: distribuição da idade

idades = df['age']

plt.hist(idades, color='Black') 


# In[29]:


# Linha: média de idade por classe 

idade_classe = df.groupby('pclass')['age'].mean()

idade_media = idade_classe.values
classes = idade_classe.index

plt.plot(classes, idade_media, c='r')
plt.show()

