# Matematica básica
import numpy as np

arr = np.array([1, 2, 3])
print(np.cumsum(arr)) # Soma acumulada

# ====================================================
# Minimo multiplo comum
x = np.lcm(4, 6) 
print(x) # 12

arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr) # Recebendo um array de entrada
print(x)

# ====================================================
# Máximo divisor comum
x = np.gcd(4, 6) 
print(x) # 2

arr = np.array([3, 6, 9])
x = np.gcd.reduce(arr) # Recebendo um array de entrada
print(x) # 3

# ====================================================
# Conjuntos
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)
print(x) # [1, 2, 3, 4, 5, 6, 7]