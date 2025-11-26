import numpy as np

a = np.random.rand(10)
print(a)

b = np.random.normal(10)
b = np.trunc(b).astype(int)
print(b)

arr = np.fix([-3.1666, 3.6667])
print(arr)

# Arredonda a partir do digito X
arr = np.around(3.1666, 2)
print(arr)
# saida = 3.17

print(np.floor([-3.1211, 12.1]))
# saida = -4. , 12. 

print(np.ceil([-3.1 , 12.1]))
# saida = -3. 13.