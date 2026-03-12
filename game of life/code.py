import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

N = 60 # grid size

# initialize the grid randomly (alive = 1, dead = 0)
grid = np.random.choice([0, 1], size=(N, N), p=[0.7, 0.3])

# function to update the grid at each step
def update(frame):
    global grid
    new_grid = grid.copy()

    for i in range(N):
        for j in range(N):
            # count alive neighbors (the 8 surrounding cells)
            neighbors = (
                grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, j] + grid[(i-1)%N, (j+1)%N] +
                grid[i, (j-1)%N]                     + grid[i, (j+1)%N] +
                grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, j] + grid[(i+1)%N, (j+1)%N]
            )

            # apply the game of life rules
            if grid[i, j] == 1:  # alive cell
                if neighbors < 2 or neighbors > 3:
                    new_grid[i, j] = 0
            else:  # dead cell
                if neighbors == 3:
                    new_grid[i, j] = 1

    grid = new_grid
    img.set_data(grid)
    return [img]

# Set up the plot
fig, ax = plt.subplots()
img = ax.imshow(grid, cmap="binary")
ax.set_title("Conway's Game of Life")
ax.axis("off")  # Hide axes

ani = FuncAnimation(fig, update, frames=200, interval=100)

# Save as GIF
writer = PillowWriter(fps=10)
ani.save("game_of_life.gif", writer=writer)

plt.show()
