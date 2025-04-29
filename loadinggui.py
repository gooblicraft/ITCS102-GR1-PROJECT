from tkinter import *
from PIL import Image, ImageTk
import time
# Create window
loadingWindow = Tk()
loadingWindow.title("loading by bestfriend")
loadingWindow.geometry("960x540")

# Load the GIF
gif = Image.open("ITCS102-GR1-PROJECT\loading ni bestfriend.gif")

frames = []
try:
    while True:
        frame = ImageTk.PhotoImage(gif.copy())
        frames.append(frame)
        gif.seek(len(frames))  # Go to next frame
except EOFError:
    pass  # No more frames

# Create label to show GIF
label = Label(loadingWindow)
label.pack()

# Animation function
frame_index = 0
def update_gif():
    global frame_index
    label.config(image=frames[frame_index])
    frame_index = (frame_index + 1) % len(frames)
    loadingWindow.after(50, update_gif) 


def newWindow(): #log in window <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<,
    loadingWindow.destroy()
    bespren = Tk()
    bespren.mainloop()

loadingWindow.after(10500, newWindow)

update_gif()  # Start animation
loadingWindow.mainloop()
