import numpy as np
import matplotlib.pyplot as plt

N = 1000

x = np.linspace(0, 100, N)
y = 10*x + 200 + np.random.normal(0, 100, N)

# Fit the date by straight line

a, b = np.polyfit(x, y, 1)  # highest power first

plt.ion()
plt.plot(x, y, 'b.')
plt.plot(x, a*x + b, 'k--')
plt.title('y = {:.1f}x + {:.1f}'.format(a, b))
plt.grid()
input()
