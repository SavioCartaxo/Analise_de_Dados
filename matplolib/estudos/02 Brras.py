#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[15]:


# Gráfico em barras

x = np.array(["A", "B", "C", "D"])
y = np.array([8, 3, 5, 2])

plt.bar(x,y ,width=0.2)
plt.show()


# In[ ]:


# Gráfico em barras de lado

x = np.array(["A", "B", "C", "D"])
y = np.array([8, 3, 5, 2])
y = np.sort(y)

plt.barh(x,y, color='r', height = 0.1)
plt.show()

