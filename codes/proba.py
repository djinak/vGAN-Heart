import numpy as np

a=np.ones((5,2), dtype=int)
b = [[1, 2, 3], [1, 2, 5]]
pad = 3
b = b[:,1:2]
print(b)