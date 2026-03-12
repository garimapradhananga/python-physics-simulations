import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


g = 9.81    #gravity 
v0 = 15     #initial speed 
angle = 60  #launch angle

#angle to radians 
import math
theta = math.radians(angle)

#Initial velocity components 
v_x = v0 * math.cos(theta)  #horizontal velocity (constant)
v_y = v0 * math.sin(theta)  #initial vertical velocity

dt = 0.01   #every loop step advances the simulation by 0.01 seconds.
t_max = 3   #total time

x = [0]   #initial x-position
y = [0]   #initial y-position

#Simulation loop
t = 0
while t < t_max:
    t += dt
    x_new = v_x * t                   #horizontal position
    y_new = v_y * t - 0.5 * g * t**2  #vertical position

    if y_new < 0:  #stops at ground
        y_new = 0

    x.append(x_new)
    y.append(y_new)

    if y_new == 0:  #stops if projectile hits ground
        break

fig, ax = plt.subplots() #creates the figure and the axes
ax.set_xlim(0, max(x)*1.1) #horizontal limits of the graph
ax.set_ylim(0, max(y)*1.2) #vertical limits of the graph
projectile, = ax.plot([x[0]], [y[0]], 'ro', markersize=8)  #red dot for projectile
path, = ax.plot([], [], 'k--')  #dashed line to show path

#update
def update(frame):
    projectile.set_data([x[frame]], [y[frame]]) 
    path.set_data(x[:frame+1], y[:frame+1])    
    return projectile, path

ani = FuncAnimation(fig, update, frames=len(x), interval=dt*1000, blit=True)
plt.title(f"Projectile Motion: {v0} m/s at {angle}°")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.show()
ani.save("projectile_motion.gif", writer="pillow")


