import matplotlib.pyplot as plt
import numpy as np
x = np.arange(10)
y = np.random.randint(20,size=(10,))
plt.plot(x,y,'c.-.')
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)
plt.show()

