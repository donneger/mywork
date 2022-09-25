import numpy as np
import matplotlib.pyplot as plt

numbers = list((0, 1, 2, 3, 4))



x = np.array([0,1,2,3,4])
plt.figure(facecolor = 'violet')
plt.plot(x, x, 'o-r', ms=10, mec = 'b', mfc = 'r', label = 'Linear')
plt.plot(x, x**2, 'o--g', ms=10, mec = 'r', mfc = 'b', label = 'Quadratic')
plt.plot(x, x**3, 'o--b', ms=10, mec = 'b', mfc = 'g', label = 'Cubed')

ax = plt.axes()
ax.set_facecolor('yellow')
plt.xticks(x)
plt.legend(fontsize = 15)
plt.title('Week 8 Lab Plotting')
plt.xlabel('Dimension (x)', fontsize = 15)
plt.ylabel('Function(y)', fontsize = 15)
plt.grid(linestyle = 'dashed')
plt.show()



