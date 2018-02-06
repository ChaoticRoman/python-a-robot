import numpy as np
import matplotlib

N = 1000

x = np.linspace(0, 100, N)
y = 10*x + 200 + np.random.normal(0, 100, N)

# Fit x, y data by straight line (polynomial fit of degree 1)
