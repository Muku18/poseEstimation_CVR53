import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

def upload_image1():
    image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if image_path:
        image = Image.open(image_path)
        image = image.resize((200, 200))
        photo = ImageTk.PhotoImage(image)
        label1.config(image=photo)
        label1.image = photo

def upload_image2():
    image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if image_path:
        image = Image.open(image_path)
        image = image.resize((200, 200))
        photo = ImageTk.PhotoImage(image)
        label3.config(image=photo)
        label3.image = photo

def upload_text1():
    text_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if text_path:
        with open(text_path, 'r') as file:
            content = file.read()
        text_area1.delete('1.0', tk.END)
        text_area1.insert(tk.END, content)
        print("Text 1 content:")
        print(content)

def upload_text2():
    text_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if text_path:
        with open(text_path, 'r') as file:
            content = file.read()
        text_area2.delete('1.0', tk.END)
        text_area2.insert(tk.END, content)
        print("Text 2 content:")
        print(content)

def generate_content():
    # Placeholder function to generate the content
    generated_image_path = "path/to/generated_image.jpg"
    generated_text = "This is the generated text."

    # Display the generated image
    generated_image = Image.open(generated_image_path)
    generated_image = generated_image.resize((200, 200))
    generated_photo = ImageTk.PhotoImage(generated_image)
    generated_label.config(image=generated_photo)
    generated_label.image = generated_photo

    # Display the generated text
    generated_text_label.config(text=generated_text)

# Create the main window
window = tk.Tk()
window.title("Image and Text Uploader")
window.geometry("1200x600")

# Create a frame for the first part (700 width)
frame1 = tk.Frame(window, width=700)
frame1.pack(side=tk.LEFT)

# Split frame1 into two equal halves vertically
frame2 = tk.Frame(frame1, width=350)
frame2.pack(side=tk.LEFT, padx=10)

# Add separator between the two halves
separator = ttk.Separator(frame1, orient='vertical')
separator.pack(side=tk.LEFT, padx=10, fill='y')

frame3 = tk.Frame(frame1, width=350)
frame3.pack(side=tk.LEFT, padx=10)

# Create a label for image 1
label1 = tk.Label(frame2)
label1.pack()

# Create a button for image 1 upload
button1 = tk.Button(frame2, text="Upload Image 1", command=upload_image1)
button1.pack(pady=10)

# Create a label for text 1
label2 = tk.Label(frame2, text="Text 1")
label2.pack()

# Create a button for text 1 upload
button2 = tk.Button(frame2, text="Upload Text 1", command=upload_text1)
button2.pack(pady=10)

# Create a text area for text 1
text_area1 = tk.Text(frame2, height=10, width=30)
text_area1.pack()

# Create a label for image 2
label3 = tk.Label(frame3)
label3.pack()

# Create a button for image 2 upload
button3 = tk.Button(frame3, text="Upload Image 2", command=upload_image2)
button3.pack(pady=10)

# Create a label for text 2
label4 = tk.Label(frame3, text="Text 2")
label4.pack()

# Create a button for text 2 upload
button4 = tk.Button(frame3, text="Upload Text 2", command=upload_text2)
button4.pack(pady=10)

# Create a text area for text 2
text_area2 = tk.Text(frame3, height=10, width=30)
text_area2.pack()

# Create a frame for the second part (500 width)
frame4 = tk.Frame(window, width=500, bg="#f0f0f0")
frame4.pack(side=tk.LEFT)

# Create a label for generated image
generated_label = tk.Label(frame4)
generated_label.pack()

# Create a label for generated text
generated_text_label = tk.Label(frame4, text="Generated Text")
generated_text_label.pack()

# Generate the content immediately
generate_content()

# Start the Tkinter event loop
window.mainloop()
