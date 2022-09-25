

import matplotlib.pyplot as plt

import numpy as np

xpoints = np.array(range(1,1001))
ypoints = xpoints*xpoints

plt.plot(xpoints, ypoints, label="Gerry1")
plt.plot(xpoints, xpoints, label="Gerry2")
plt.legend()

randompoints = np.random.randint(1, 1000, 1000)
plt.scatter(xpoints, randompoints)

plt.show()


