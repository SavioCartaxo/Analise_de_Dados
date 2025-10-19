#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np


# In[ ]:


y = np.array([35, 25, 25, 15])

nomes = ["a", 'b', 'c', 'd']
afastamento = [0,0,0,0.2]

plt.pie(y, labels=nomes, explode=afastamento, startangle = 180) # gira o grafico
plt.show() 


# In[50]:


y = np.array([35, 25, 25, 15])

nomes = ["a", 'b', 'c', 'd']
cores = ["blue", "Green", "cyan", "DarkBlue"]

plt.pie(y, shadow = True, colors=cores, labels=nomes)
plt.legend(title = "Letras:")
plt.show() 

