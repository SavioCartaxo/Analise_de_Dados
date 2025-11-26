import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)

# Ele tem o argumento order:
print("")
# Padrão = "C" pois percorre por linha
# Pode ser usado "F" de argumento, para printar por coluna

for x in np.nditer(arr, order="F"):
  print(x)
print("")

# Pode modificar os valores durante as iterações usando op_flags=['readwrite']

arr = np.array([1, 2, 3])
for x in np.nditer(arr, op_flags=["readwrite"]):
    x[...] = x * 2  # Modifica os valores

print(arr)

# Iterar em mais de um array ao mesmo tempo

a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])

for x, y in np.nditer([a,b]):
   print(x,y)

# enumeratede em nditer == ndenumerate

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)