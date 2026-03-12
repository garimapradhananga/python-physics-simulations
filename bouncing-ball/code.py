import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

g = 9.81        # gravity (m/s^2)
dt = 0.02       # time step (seconds)

energy_loss = [0.5, 0.7, 0.9]  # three balls with different bounce heights
colors = ['r', 'g', 'b']

# Initial conditions
y_init = 10.0   
v_init = 0.0    # initial vertical velocity

balls_data = []

for e in energy_loss:
    y = y_init
    v = v_init
    y_values = [y]

    for i in range(500):
        v -= g * dt
        y += v * dt

        if y <= 0:
            y = 0
            v = -e * v

        y_values.append(y)

    balls_data.append(y_values)

fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, y_init * 1.2)
ax.set_ylabel("Height (m)")
ax.set_title("Bouncing Balls with Energy Loss")

# Create ball plots and trail plots
balls = []
trails = []
for i, color in enumerate(colors):
    ball_plot, = ax.plot([0.5 + i*0.1], [balls_data[i][0]], 'o', color=color, markersize=10)
    trail_plot, = ax.plot([], [], '--', color=color, alpha=0.5)
    balls.append(ball_plot)
    trails.append(trail_plot)

def update(frame):
    for i in range(len(balls_data)):
        balls[i].set_data([0.5 + i*0.1], [balls_data[i][frame]])
        trails[i].set_data([0.5 + i*0.1]*frame, balls_data[i][:frame])
    return balls + trails

ani = FuncAnimation(fig, update, frames=len(balls_data[0]), interval=dt*1000)

plt.show()
ani.save("bouncing_ball.gif", writer="pillow")
