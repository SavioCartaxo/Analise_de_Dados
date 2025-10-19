import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,10])
print(a)

b = np.zeros((4,2), int)
print(b)

c = np.empty((5,3))
print(c)

d = np.arange(1, 10, 12)
print(d)

e = np.linspace(0, 100, num=21, endpoint=True).astype(int)
print(e)

f = np.empty((8,4,2))
print(f.shape)
print(f.ndim)
print(f.size)

g = a[:,np.newaxis]
print(g)

h = np.concatenate((a,a,a))
print(h)

i = np.vstack((b,b))
print(i)

j = a[a>=6]
print(j)

j2 = a[a % 2 == 0]
print(j2)

k = a

print(np.sum(k))
print(np.min(k))
print(np.max(k))
print(np.mean(k))
print(np.median(k))

from numpy.random import default_rng

l = a*a
print(l)

m = default_rng()
m = m.integers(2, size=(2,5))
print(m)

n = a.reshape(5,2)
print(n)

o = np.random.randint(50,151, size=12)
o = np.sort(e)
print(e)