import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
from PIL import Image, ImageTk
from playsound import playsound

class VideoPlayer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Video Player")

        self.video_source = None
        self.video = None
        self.width = 0
        self.height = 0

        self.canvas_width = 800  # Specify the desired width of the canvas
        self.canvas_height = 600  # Specify the desired height of the canvas

        self.canvas = tk.Canvas(self.window, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        self.select_button = tk.Button(self.window, text="Select Video", command=self.select_video)
        self.select_button.pack()

        self.play_button = tk.Button(self.window, text="Play", command=self.play_video)
        self.play_button.pack()

        self.window.mainloop()

    def select_video(self):
        # Open a file dialog to select a video file
        file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])

        if file_path:
            self.video_source = file_path

            # Open the selected video file
            self.video = cv2.VideoCapture(self.video_source)

            # Get the video width and height
            self.width = self.video.get(cv2.CAP_PROP_FRAME_WIDTH)
            self.height = self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)

            messagebox.showinfo("Video Uploaded", "Video uploaded successfully.")

    def play_video(self):
        if self.video_source:
            # Set the video capture object to the first frame
            self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)

            # Start the video playback in a separate thread
            self.window.after(0, self.play_video_thread)

    def play_video_thread(self):
        # Read a frame from the video source
        ret, frame = self.video.read()

        if ret:
            # Convert the frame to RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Resize the frame to fit the canvas
            frame_resized = cv2.resize(frame_rgb, (self.canvas_width, self.canvas_height))

            # Convert the resized frame to PIL Image format
            image = Image.fromarray(frame_resized)

            # Convert the PIL Image to Tkinter format
            photo = ImageTk.PhotoImage(image)

            # Display the frame on the canvas
            self.canvas.create_image(0, 0, image=photo, anchor=tk.NW)
            self.canvas.image = photo

            # Play the sound of the video
            sound_path = self.video_source
            playsound(sound_path, block=False)

            # Schedule the next frame update
            self.window.after(1, self.play_video_thread)

# Create an instance of the VideoPlayer class
player = VideoPlayer()
