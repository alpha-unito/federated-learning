import numpy as np
from sys import getsizeof

a = [np.zeros(10) for i in range(10)]

print(getsizeof(a))

tot = 0

for n in a:
    tot += n.nbytes

print(tot)

