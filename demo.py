import numpy as np

# Example function
x = np.linspace(0, 10, 1000)
y = np.sin(x)

# Numerical derivative dy/dx
dy_dx = np.gradient(y, x)

print(dy_dx[:5])  # first few values
