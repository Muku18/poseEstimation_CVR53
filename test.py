import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create the figure and axes
fig, ax = plt.subplots()

# Create the initial plot
x = np.linspace(0, 2*np.pi, 200)
y = np.sin(x)
line, = ax.plot(x, y)

# Define the update function
def update(num):
    # Update the data
    line.set_ydata(np.sin(num * x))

    # Return the updated line object
    return line,

# Create the animation object
ani = animation.FuncAnimation(fig, update, frames=100, interval=50)

# Show the plot
plt.show()
