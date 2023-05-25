import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

videox = []
videoy = []
with open('poseEstimation.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.rstrip()
        v = list(line.split(" "))
        print(v)
        videox.append(float(v[0])/37.3)
        videoy.append(float(v[1])/37.5)
print(videox)
print(videoy)

m = len(videox)
n = len(videoy)
print(m,n)

i = 0
# define the initial position of the point
startx, starty = 18.6, 8.88
positions = [(startx, starty)]  # list to store the positions of the point

# create a figure and axis
fig, ax = plt.subplots()

# create a line object
line, = ax.plot([], [])

# create a scatter object for the point
point = ax.scatter(startx, starty, s=50, color='red')


# define the update function for the animation
def update(frame):
    # update the position of the point
    global x,y,i,startx,starty
    i = i + 1
    if i == 40:
        exit()
    x = videox[i]
    y = videoy[i]
    positions.append((x, y))  # add the new position to the list
    point.set_offsets((x, y))  # update the position of the scatter object

    # update the line object with the new positions
    line.set_data(*zip(*positions))

    # set the axis limits
    ax.set_xlim(0, 34.3)
    ax.set_ylim(0, 19.2)
    t = (x - startx)**2 + (y-starty)**2
    velocity = math.sqrt(t)
    print("Current coordinates: ({}, {})".format(x, y))
    print("Velocity: ",velocity)
    startx = x
    starty = y

    return point, line


# create the animation
ani = FuncAnimation(fig, update, frames=10, interval=1000, blit=True)

# show the animation
plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
#
# # Define the figure and axis for the plot
# fig, ax = plt.subplots()
#
# # Initialize the point and line objects
# point, = ax.plot([], [], 'ro')
# line, = ax.plot([], [], 'b--')
#
#
# # Define the function to update the plot for each frame
# def update(frame):
#     # Get the current x and y coordinates of the point
#     x, y = point.get_data()
#
#     # Get the new x and y coordinates of the point
#     x_new = np.random.randint(0, 10)
#     y_new = np.random.randint(0, 10)
#
#     # Append the new coordinates to the existing coordinates
#     x = np.append(x, x_new)
#     y = np.append(y, y_new)
#
#     # Update the point and line objects with the new coordinates
#     point.set_data(x_new, y_new)
#     line.set_data(x, y)
#
#     # Display the coordinates of the point every second
#     if frame % 30 == 0:
#         print("Current coordinates: ({}, {})".format(x_new, y_new))
#
#     return point, line
#
#
# # Define the animation
# ani = animation.FuncAnimation(fig, update, frames=100, interval=1000, blit=True)
#
# # Show the plot
# plt.show()



