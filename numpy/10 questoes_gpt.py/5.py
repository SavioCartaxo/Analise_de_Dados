# 5. Gere um array contendo 10 números igualmente espaçados entre 5 e 50.

import numpy as np

a = np.linspace(5, 50, num=10, endpoint=True)

print(a)