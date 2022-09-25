import numpy as np

import matplotlib.pyplot as plt
'''
normdata = np.random.normal(size = 1000)

plt.hist(normdata)
plt.show()
'''

fruit = np.array(['apples','orange', 'pears'])

numbers = np.array([23, 77, 200])

plt.pie(numbers, labels = fruit)
plt.legend()
plt.show()