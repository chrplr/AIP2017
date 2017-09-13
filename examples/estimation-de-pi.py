from random import random

N = 100000
print(4 * sum([(random()**2 + random()**2 <= 1) for _ in range(N)])/N)

