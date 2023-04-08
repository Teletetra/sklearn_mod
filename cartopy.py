import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import sys
# Create a figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a scatter plot with random data
n = 100
x = np.random.rand(n)
y = np.random.rand(n)
z = np.random.rand(n)
sc = ax.scatter(x, y, z)

# Define the update function for the animation
def update(i):
    # Generate new data for the scatter plot
    x = np.random.rand(n)
    y = np.random.rand(n)
    z = np.random.rand(n)
    sc._offsets3d = (x, y, z)
    return sc,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show the plot
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()