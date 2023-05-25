# =====================module import=================================
import time
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
root = Tk()
root.geometry("1174x698+50+0")
root.title("COMPUTER VISION")
root.resizable(False, False)
root.configure(bg="#074463")
from PIL import Image, ImageTk
import random
colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
def color():
    fg = random.choice(colors)
    Sliderlabel.config(fg=fg)
    Sliderlabel.after(2, color)


# =====================================================================


# ==============================INTRO LABEL FUNCTION===================
def introlabel():
    global count, text
    if (count >= len(Ss)):
        count = 0
        text = ''
        Sliderlabel.config(text=text)
    else:
        text = text + Ss[count]
        Sliderlabel.config(text=text)
        count = count + 1
    Sliderlabel.after(200, introlabel)


# ======================================================================

Ss = "POSE ESTIMATION OF SATELLITE"
text = ''
count = 0

AR = "ESTIMATE THE POSES OF SATELLITE AND PORT IN AN SATELLITE VIDEO"
textlabel = Label(root, bd=5, relief=GROOVE, text=AR, bg="gold", font=("chillar", 20, "bold"))
textlabel.place(x=110, y=200)

Sliderlabel = Label(root, text=Ss, font=("new times roman", 25, "bold"), bd=5, relief=GROOVE, width=30)
Sliderlabel.pack(side=TOP, fill=X)
introlabel()
color()
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

i = 0
# define the initial position of the point
startx, starty = 18.6, 8.88
def predictsatellite():
    import tkinter as tk
    new_window = tk.Tk()
    new_window.geometry("1174x698+50+0")
    new_window.title("COMPUTER VISION")
    new_window.resizable(False, False)
    new_window.configure(bg="#074463")
    # Start the main event loop
    new_window = tk.Label(new_window, text="This is a new window!")
    new_window.pack()
    new_window.mainloop()
def satellitepose():
    predictsatellite()

posebutton = Button(root, command=satellitepose, activebackground="crimson", text="SATELITTE", font=("chillar", 15, "bold"),
                     bg="green", bd=5, relief=GROOVE)
posebutton.place(x=200, y=380)

ip = 0
startpx, startpy = 21.742627345844507, 11.413333333333334
def portpose():
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation
    import math

    portx = []
    porty = []
    with open('uu.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.rstrip()
            v = list(line.split(" "))
            print(v)
            portx.append(float(v[0]) / 37.3)
            porty.append(float(v[1]) / 37.5)
    print(portx)
    print(porty)

    mp = len(portx)
    np = len(porty)
    print(mp, np)


    # define the initial position of the point
    positionps = [(startpx, startpy)]  # list to store the positions of the point

    # create a figure and axis
    figp, axp = plt.subplots()

    # create a line object
    linep, = axp.plot([], [])

    # create a scatter object for the point
    pointp = axp.scatter(startpx, startpy, s=50, color='blue')

    # define the update function for the animation
    def updatep(frame):
        # update the position of the point
        global x, y, ip, startpx, startpy
        ip = ip + 1
        if ip == 24:
            exit()
        x = portx[ip]
        y = porty[ip]
        positionps.append((x, y))  # add the new position to the list
        pointp.set_offsets((x, y))  # update the position of the scatter object

        # update the line object with the new positions
        linep.set_data(*zip(*positionps))

        # set the axis limits
        axp.set_xlim(0, 35)
        axp.set_ylim(0, 20)
        t = (x - startpx) ** 2 + (y - startpy) ** 2
        velocityp = math.sqrt(t)
        print(f"FRAME --- {ip*4}")
        print("Current coordinates: ({}, {})".format(x, y))
        print(f"Velocity: {velocityp}m/s")
        print()
        startpx = x
        startpy = y

        return pointp, linep

    # create the animation
    ani = FuncAnimation(figp, updatep, frames=10, interval=1000, blit=True)

    # show the animation
    plt.xlabel('metre')
    plt.ylabel('metre')
    plt.title('port pose')
    plt.show()


portbutton = Button(root, command=portpose, activebackground="crimson", text="PORTPOSE", font=("chillar", 15, "bold"),
                     bg="green", bd=5, relief=GROOVE)
portbutton.place(x=700, y=380)




# =======================================================================



root.mainloop()