import pandas as pd
import numpy as np

a = np.arange(0, 101)
myvar = pd.Series(np.arange(0, 301, 3), index = a)

print(myvar)
print(myvar[1])