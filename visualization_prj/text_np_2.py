import numpy as np
np.random.seed(1000)
arr = np.random.randint(1,10,size=(3,4))
print(arr)
print(np.sum(arr))
print(np.average(arr))
print(np.var(arr)**(1/2))
print(np.std (arr))

