import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0,6,0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.title('sin and cos')
plt.plot(x,y1, label='sin')
plt.plot(x,y2, label='cos', linestyle='--')
plt.xlabel("x")
plt.ylabel("y")
plt.show()