import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a blank figure and axis
fig, ax = plt.subplots()

# Set the axis limits
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1, 1)

# Initialize the line plot
line, = ax.plot([], [], lw=2)

# Function to initialize the animation
def init():
    line.set_data([], [])
    return line,

# Function to update the animation frame
def update(frame):
    x_data = np.linspace(0, 2 * np.pi, 1000)
    y_data = np.sin(x_data + frame * 0.1)
    line.set_data(x_data, y_data)
    return line,

# Create the animation
ani = FuncAnimation(fig, update, frames=100, init_func=init, blit=True)

# Display the animation
plt.show()

