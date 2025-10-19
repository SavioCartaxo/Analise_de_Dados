import numpy as np

# Arrays

# 1 dimensão é chamado de Vetor
# 2 dimensões é chamado de matriz
# 3 dimensões ou mais é chamado de tensor

## criando um array

a = np.array([1,2,3,4,5,6])
b = [1,2,3,4,5,6]

print(a) # é um array
print(type(a))
print(b) # é uma lista
print(type(b))

# Arrays com np.zeros
  # Arrays vazios

zero_arrays = np.zeros(shape = (5,3,6)) # Tensor

print(zero_arrays)

# Arrays com números aleatórios não nulos

nao_vazio = np.empty(3)
# Se quiser mais de uma dimensão, da uma túpla de argumento:
# nao_vazio = np.empty((3, 2, 4))
print(nao_vazio)

# Array com o range

arr = np.arange(10)

# cria array do 0 ao 9
# np.arrange(start, stop, passo(step), type)

arr = np.arange(1, 11, 2, float)
print(arr)

# Sequencia linear

arrray_linear = np.linspace(0, 100, num=20,endpoint=False)
#pega do 0 ao 100(com o 100=False(não aparece)), sendo que ele pega 20 desses numeros
print(arrray_linear)

# Descobrindo o tamanho de um Array

print(zero_arrays.shape) # printa o shape
print(zero_arrays.size)  # printa o número de elementos
print(zero_arrays.ndim)  # printa o número de dimensões

# Transformando um vetor em uma matriz

a = np.array([1,2,3,4,5])
a2 = a[np.newaxis,:] # Transforma uma matriz 5 em uma 1x5
print(a2) # 2 dimensões (1,5)

a3 = a[:,np.newaxis] # cria matriz com cada elemento
print(a3) # 2 dimensões (5,1)

print(a2[0][0]) # Isso eu já sei

# Concatenando Arrays

a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.concatenate((a,b)))
print(np.concatenate((a,a)))

# Concatenando verticalmente (matrizes)

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

c = np.vstack((a,b))  # Empilhamento vertical
print(c)

# Consultando Arrays

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

maior_5 = a[a>5]
print("\n",maior_5)

# operações com Array

arr = np.array([1,2,3,4,5])

print(np.mean(arr))   # Média: 3.0
print(np.median(arr)) # Mediana: 3
print(np.std(arr))    # Desvio padrão: 1.41
print(np.sum(arr))    # Soma: 15
print(np.min(arr))    # Mínimo: 1
print(np.max(arr))    # Máximo: 5

# Outra forma de fazer arrays com números aleatórios

from numpy.random import default_rng

rng = default_rng()
aleatorio = rng.integers(10,size= (2,4)) # números inteiros menores que 10 em uma matriz 2x4
print(aleatorio)

# Comparando tempo de execução de um Array e uma lista

from time import process_time

lista_a = list(rng.integers(10,100,1000000))
# c = []
# c = lista_a*lista_b # Essa operação não é possivel com listas

c = []

t1 = process_time()
for i in range(len(lista_a)):
    c.append(lista_a[i]*lista_a[i])
t2 = process_time()

print(t2 - t1) # demorou 0.265625 segundos

a = rng.integers(10,100,1000000)

t1 = process_time()
c = a * a
t2 = process_time()
print(t2 - t1) # demorou 0.015625 segundos, cerca de 20x mais rápido

# Acessando elementos individuais ou partes do array

arr = np.array([10, 20, 30, 40, 50])

print(arr[2])    # Saída: 30
print(arr[1:4])  # Saída: [20 30 40]
print(arr[-2:])  # Saída: [40 50]

# Alterando o formato do Array

arr = np.array([1, 2, 3, 4, 5, 6])
arr_reshape = arr.reshape(2, 3) # Transformando em uma matriz 2x3

print(arr_reshape)

# Multiplicação de matrizes

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

C = np.dot(A, B)

#C_11 = (1 × 5) + (2 × 7) = 5 + 14 = 19  
#C_12 = (1 × 6) + (2 × 8) = 6 + 16 = 22  
#C_21 = (3 × 5) + (4 × 7) = 15 + 28 = 43  
#C_22 = (3 × 6) + (4 × 8) = 18 + 32 = 50  

print(C)

# Resumo

"""
✅ Criar e manipular arrays
✅ Fazer slicing e reshape
✅ Calcular médias, desvios padrão, somas
✅ Gerar números aleatórios
✅ Usar máscaras booleanas  # print(arr[arr > 25])
✅ Fazer operações de álgebra linear
"""