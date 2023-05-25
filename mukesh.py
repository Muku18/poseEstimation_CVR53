import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
from fpdf import FPDF
import math
import numpy as np

# Create the Tkinter window
root = tk.Tk()
root.geometry("1200x600+50+0")
root.title("COMPUTER VISION")
root.resizable(False, False)
root.configure(bg="#074463")
root.title("Divided Window")

# Set the width of the left and right frames
left_frame_width = 600
right_frame_width = 300

# Create a PanedWindow widget to divide the window
paned_window = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
paned_window.pack(fill=tk.BOTH, expand=True)

# Create the left frame
left_frame = ttk.Frame(paned_window, width=left_frame_width)
paned_window.add(left_frame)

# Create a separator between the frames
separator = ttk.Separator(paned_window, orient=tk.VERTICAL)
paned_window.add(separator)

# Create the right frame
right_frame = ttk.Frame(paned_window, width=right_frame_width)
paned_window.add(right_frame)

# Define the initial position of the point
startx, starty = 18.6, 8.88

videox = []
videoy = []
with open('poseEstimation.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.rstrip()
        v = list(line.split(" "))
        videox.append(float(v[0]) / 37.3)
        videoy.append(float(v[1]) / 37.5)

m = len(videox)
n = len(videoy)

positions = [(startx, starty)]  # list to store the positions of the point

# create a figure and axis
fig, ax = plt.subplots(figsize=(5, 4), dpi=100)

# create a line object
line, = ax.plot([], [])

# create a scatter object for the point
point = ax.scatter(startx, starty, s=50, color='red')

# create a heatmap axis
ax2 = fig.add_axes(ax.get_position(), frameon=False)
ax2.set_xticks([])
ax2.set_yticks([])

# Function to update the plot and table
def update(frame):
    # Update the position of the point
    global x, y, startx, starty
    x = videox[frame]
    y = videoy[frame]
    positions.append((x, y))  # add the new position to the list
    point.set_offsets((x, y))  # update the position of the scatter object

    # Update the line object with the new positions
    line.set_data(*zip(*positions))

    # Set the axis limits
    ax.set_xlim(0, 34.3)
    ax.set_ylim(0, 19.2)

    t = (x - startx) ** 2 + (y - starty) ** 2
    velocity = math.sqrt(t)

    frame_label.config(text=f"Frame: {frame*15}")
    velocity_label.config(text=f"Velocity: {velocity} m/s")
    coordinates_label.config(text=f"Coordinates: ({x}, {y})")

    # Insert data into the table
    table.insert('', 'end', values=(frame*15, velocity, f"({x}, {y})"))

    startx = x
    starty = y

    # Update the heatmap
    heatmap, xedges, yedges = np.histogram2d(videox[:frame+1], videoy[:frame+1], bins=50)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    ax2.imshow(heatmap.T, origin='lower', extent=extent, cmap='hot')

    return point, line

# Create a FigureCanvasTkAgg widget
canvas_left = FigureCanvasTkAgg(fig, master=left_frame)
canvas_left.get_tk_widget().pack()

# Variable to track if animation is running
animation_running = False
ani = None

# Function to start the animation
# Function to start the animation
def start_animation():
    global animation_running, ani, current_frame
    if not animation_running:
        current_frame = 0
        if ani is not None:
            ani.event_source.start()
        else:
            ani = FuncAnimation(fig, update, frames=range(current_frame, m), interval=1000, blit=True)
        animation_running = True


# Function to stop the animation
# Function to stop the animation
def stop_animation():
    global animation_running, ani
    if animation_running:
        ani.event_source.stop()
        animation_running = False


# Create the Start button in the left frame
start_button = ttk.Button(left_frame, text="Start", command=start_animation)
start_button.place(x=10, y=410, height=50, width=150)

# Create the Stop button in the left frame
stop_button = ttk.Button(left_frame, text="Stop", command=stop_animation)
stop_button.place(x=170, y=410, height=50, width=150)

# Create the table in the right frame
table = ttk.Treeview(right_frame, columns=('Frame', 'Velocity', 'Coordinates'), show='headings')
table.heading('Frame', text='Frame')
table.heading('Velocity', text='Velocity')
table.heading('Coordinates', text='Coordinates')

# Add horizontal and vertical scrollbars to the table
table_scrollbar_y = ttk.Scrollbar(right_frame, orient='vertical', command=table.yview)
table_scrollbar_x = ttk.Scrollbar(right_frame, orient='horizontal', command=table.xview)
table.configure(yscrollcommand=table_scrollbar_y.set, xscrollcommand=table_scrollbar_x.set)

table.pack(padx=10, pady=(10, 0), fill='both', expand=True)
table_scrollbar_y.pack(side='right', fill='y')
table_scrollbar_x.pack(side='bottom', fill='x')

# Create labels for displaying details in the right frame
frame_label = ttk.Label(right_frame, text='Frame:')
frame_label.pack(padx=10, pady=(20, 5))
velocity_label = ttk.Label(right_frame, text='Velocity:')
velocity_label.pack(padx=10, pady=5)
coordinates_label = ttk.Label(right_frame, text='Coordinates:')
coordinates_label.pack(padx=10, pady=5)

# Create a search function
def search():
    keyword = search_entry.get()
    if keyword:
        found_items = table.get_children()
        for item in found_items:
            values = table.item(item, 'values')
            frame_value = values[0]
            if keyword == str(frame_value):
                table.selection_set(item)
                table.focus(item)
                table.see(item)
                break

# Create a search entry field
search_entry = ttk.Entry(right_frame, width=10)
search_entry.pack(padx=10, pady=(10, 0))

# Create a search button
search_button = ttk.Button(right_frame, text='Search', command=search)
search_button.pack(padx=10, pady=5)

# Function to generate a PDF file
def generate_pdf():
    # Create a PDF object
    pdf = FPDF()

    # Add a page to the PDF
    pdf.add_page()

    # Set the font and font size
    pdf.set_font("Arial", size=12)

    # Add the table headers
    pdf.cell(40, 10, "Frame", border=1)
    pdf.cell(40, 10, "Velocity", border=1)
    pdf.cell(80, 10, "Coordinates", border=1)
    pdf.ln()

    # Iterate over the table data
    for item in table.get_children():
        values = table.item(item, 'values')
        frame = values[0]
        velocity = values[1]
        coordinates = values[2]
        pdf.cell(40, 10, str(frame), border=1)
        pdf.cell(40, 10, str(velocity), border=1)
        pdf.cell(80, 10, str(coordinates), border=1)
        pdf.ln()

    # Save the PDF file
    pdf.output("data.pdf")
    messagebox.showinfo("PDF Generated", "PDF generated successfully.")


# Create a Generate PDF button
generate_pdf_button = ttk.Button(right_frame, text='Generate PDF', command=generate_pdf)
generate_pdf_button.pack(padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
