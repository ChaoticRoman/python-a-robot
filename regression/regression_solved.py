import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

N = 1000

x = np.linspace(0, 100, N)
y = 10*x + 200 + np.random.normal(0, 100, N)

# Fit x, y data by straight line (polynomial fit of degree 1)

a, b = np.polyfit(x, y, 1)  # highest power first, i.e. y = ax + b

plt.plot(x, y, 'b.')
plt.plot(x, a*x + b, 'k--')
plt.title('y = {:.1f}x + {:.1f}'.format(a, b))
plt.grid()

plt.savefig('result.svg')
