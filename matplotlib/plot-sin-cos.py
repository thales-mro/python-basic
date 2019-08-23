import matplotlib.pylab as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 100)

plt.subplot(2,2,1)
plt.plot(x, np.sin(x))
plt.xlabel('angle [rad]')
plt.ylabel('sin(x)')

plt.subplot(2, 2, 2)
plt.plot(x, np.cos(x))
plt.xlabel('angle [rad]')
plt.ylabel('cos(x)')

plt.axis('tight')
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x) * np.sin(x))
plt.title('sin(x)*cos(x)')
plt.tight_layout()
plt.show()