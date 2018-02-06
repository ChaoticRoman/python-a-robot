import numpy as np

N = 1000
x = np.linspace(0, 100, N)
y = 10*x + 200 + np.random.normal(0, 100, N)

# Fit the date by straight line and plot it
