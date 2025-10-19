import numpy as np

a = np.arange(1,10)
print(a)

b = np.zeros((5,10),int)
print(b)

c = np.array([1]*7)
print(c)

d = np.linspace(5, 50, num=10, endpoint=True).astype(int)
print(d)

e = np.random.randint(0,101, size=10)
e = np.sort(e)
print(e)

f = a.reshape((3,3))
print(f)

g = a[::-1]
print(g)

h = a[a % 2 == 0]
print(h)

i = np.random.randint(0,101, size=15)
i = i[i>50]
print(i)

a[:5] = 99
print(a)

"""
4. Operações Matemáticas
Crie dois arrays de mesmo tamanho e realize as operações: soma, subtração, multiplicação e divisão entre eles.
"""
a = np.array([1,2,3,4,5,6,7,8,9,10])
b = np.array([1,2,3,4,5,6,7,8,9,10])

"""
Calcule a média, o máximo, o mínimo e o desvio padrão de um array aleatório com 15 números entre 1 e 100.
"""

# Não sabia disso
a = np.random.uniform(1,101,size=10)
print(np.max(a))
print(np.min(a))
print(np.std(a))
print(np.mean(a))
print(np.median(a))

"""
Normalize um array para que seus valores fiquem entre 0 e 1.
"""

arr = np.random.randint(0,100, size=3)
normalizado = (arr - np.min(arr))/ (np.max(arr) - np.min(arr))
print(normalizado)

"""
5. Matrizes (Arrays Multidimensionais)
Crie uma matriz 3x3 com valores de 1 a 9.
"""

a = np.arange(1,10)
a = a.reshape((3,3))
print(a)

"""
Crie uma matriz identidade de tamanho 4x4.
"""

a = np.eye(4)
print(a)

# Multiplique duas matrizes 3x3 geradas aleatoriamente.

a = np.random.randint(1, 11, size=(3,3))
b = np.random.randint(1, 11, size=(3,3))
print("\n",a*b)

#Encontre a soma de cada linha e de cada coluna de uma matriz 4x4.
print(a)
print(np.sum(a, axis=1))

# 6. Aplicações Avançadas

# Gere um array de 100 números aleatórios e substitua todos os valores menores que 30 por 0.

a = np.random.randint(0, 101, size=100)
print(a)
a[a < 30] = 0
print(a)

# Crie uma matriz 5x5 e substitua todos os valores da borda por 1 e o centro por 0.

a = np.ones((5,5))
a[2, 1:4] = 0
print(a)

# Gere uma matriz 6x6 com números aleatórios e encontre a posição do maior valor.
# Muito avançado

"""
Gere um array de 20 elementos aleatórios e conte quantas vezes cada valor aparece nele."
"""