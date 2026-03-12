import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Lorenz system parameters
sigma = 10
rho = 28
beta = 8 / 3

dt = 0.01
steps = 10000

# Arrays
x = np.zeros(steps)
y = np.zeros(steps)
z = np.zeros(steps)

# Initial conditions
x[0], y[0], z[0] = 0.1, 0.0, 0.0

# Lorenz equations
for i in range(steps - 1):
    x[i+1] = x[i] + sigma * (y[i] - x[i]) * dt
    y[i+1] = y[i] + (x[i] * (rho - z[i]) - y[i]) * dt
    z[i+1] = z[i] + (x[i] * y[i] - beta * z[i]) * dt

# Color based on time
colors = np.linspace(0, 1, steps)

# 3D plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(x, y, z, c=colors, cmap='plasma', s=1)

ax.set_title("Butterfly Effect (Lorenz Attractor)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.savefig("butterfly_effect.png", dpi=300)

plt.show()
