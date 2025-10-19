import numpy as np
from time import process_time

t1 = process_time()
a = np.random.randint(0,11, size=(1_000_000))

mascara = a > 4

conta_true = np.count_nonzero(mascara == True)
conta_fals = 1_000_000 - conta_true

if conta_true > conta_fals: print("Lucro")
else: print('Prejuizo')

t2 = process_time()

print(t2 - t1)

# and == &
# or == |