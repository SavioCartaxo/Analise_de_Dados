#!/usr/bin/env python
# coding: utf-8

# In[20]:


import matplotlib.pyplot as plt
import numpy as np

# Plots
x = np.arange(1, 101)
y = np.random.randint(0, 100, size=100)
plt.plot(x, "X-.m", c="red", ms=5)
plt.plot(y, "o:g", c="b", mec="r", ms=5)

# Nomes
plt.title("Número aleatórios", loc="left")
plt.xlabel("INDEX")
plt.ylabel("N° Aleatório")

plt.show()

