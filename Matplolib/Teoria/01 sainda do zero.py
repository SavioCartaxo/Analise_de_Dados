#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [2,3,4,3]
plt.plot(x,y)
plt.title("Linha azul que desce")
plt.xlabel("Eixo x")
plt.ylabel("eixo Y")
plt.show()


# In[2]:


# Para plotar apenas o ponto, utiliza-se o argumento 'o'
plt.plot(x, y, 'o')
plt.show()


# In[3]:


# Se dermos apenas um argumento, ele vai usar o index como eixo X

plt.plot(y)
plt.show


# In[4]:


# Marker (marcadores)

plt.plot(y, marker='o')
plt.show()


# In[5]:


# Tipos de linha
import numpy as np

x = np.array([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])

plt.plot(x, 'X-.m', ms=10, mec='r', mfc='pink',linewidth=2)
# marcador, tipo de linha, cor

# Cor:  r(ed), g(reen), b(lue), c(iano), m(agenta), y(ellow), k(black), w(hite) 
# Tipo de linha : - -- -.

# Mark size(ms) = tamanho do mark
# Mark Color(mec) = cor do marcador

# mfc = cor os marcadores

# c = cor da linha
# linewidth = grossura da linha


# In[6]:


# Pode escolher cores se der um código hexadecimal de argumento ou nome das cores

plt.plot(x, 'o--r', c="DarkBlue", mec="r", ms=8, mfc="black")


# In[7]:


# Plotando 2 gráficos ao mesmo tempo 

x = np.array([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])
y = -x
plt.plot(x, 'X-.m', ms=10, mec='r', mfc='pink',linewidth=2)
plt.plot(y, 'o--r', c="DarkBlue", mec="r", ms=8, mfc="black")

plt.show()


# In[8]:


# Sobre os nomes que podem ser dados
font1 = {'family':'serif','color':'hotpink','size':18}
font2 = {'family':'serif','color':'black','size':12}

# Criando os plots
plt.plot(x, 'X-.m', ms=10, mec='r', mfc='pink',linewidth=2)
plt.plot(y, 'o--r', c="DarkBlue", mec="r", ms=8, mfc="black")

# Dando titulos aos eixos e ao gráfico
plt.title("Gráfico de X por Y", fontdict=font1, loc='left')
plt.xlabel("Números aleatórios", fontdict=font2)
plt.ylabel("Index", fontdict=font2)

plt.show()


# loc pode receber: left, right
# 

# In[9]:


# Grade

plt.grid(axis="x", color='green', linestyle='-.', linewidth = 0.5) #se quiser a linha só em uma direção, argmento axis
# axis="x" ou axis="y"
plt.show() 


# In[10]:


# plot 1
x = np.arange(1, 6)
y = np.arange(0,5)
plt.subplot(1,2,1) # (n_linhas, n_colunas, índice)
plt.plot(x, x)

# plot 2

plt.subplot(1,2,2)
plt.plot(y,y)
plt.title("Gráfico 2")

# Geral
plt.suptitle("Dois gráficos")
plt.show()


# In[11]:


# marcando apenas os pontos sem fazer desenhos

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color="red")

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color="black")


# In[12]:


# Estudar mapa de cores(colormap) do Matplotlib

x = np.random.randint(1, 101, size=100)
y = np.random.randint(1, 11, size=100)

colors = np.linspace(0, 101, num=100)

plt.scatter(x, y, c=colors, cmap='Blues_r')

plt.colorbar()

# Alguns extras para deixar o mapa mais bonitinho
plt.title("AZUL", loc="left", c="DarkBlue")
plt.xlabel("Entre 1 e 100", c="b")
plt.ylabel("Entre 1 e 10", c="b")

plt.show()


# In[ ]:


# plotando o taanho por tamanho/importancia

x = np.random.randint(1, 101, size=13)
y = np.random.randint(1, 11, size=13)
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes,alpha=0.5) # alpha = transparência

plt.show()

