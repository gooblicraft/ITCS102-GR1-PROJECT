# import tkinter as tk
# from tkinter import *

# window = tk.Tk()
# window.geometry("300x300")
# window.title("LOG IN")




# username = tk.Label(window)
# username.pack()
# entry = tk.Entry()
# entry.insert(0, "Username")
# entry.pack()

# password = tk.Label(window)
# password.pack()
# entry = tk.Entry()
# entry.insert(0, "password")
# entry.pack()

# button = tk.Button(window, text="Log in ", width=25, bg="blue",fg= "white", command=window.destroy)
# button.pack(pady=10)

# # Frame to hold the Checkbutton
# options_frame = tk.Frame(window)
# options_frame.pack(fill="x", pady=(0, 10))  # Space below Entry

# # Checkbutton on the left side
# var1 = IntVar()
# var2 = IntVar()
# cb1 = tk.Checkbutton(options_frame, text="Remember Me", variable=var1)
# cb1.pack(side="left", padx=10)

# forgot_pw = tk.Label(options_frame, text="Forgot Password?", fg="blue", cursor="hand2")
# forgot_pw.pack(side="right", padx=10)

# footer_label = tk.Label(window, text="Property of Karl Oabel of BSIT 1A.", bg="white", fg="gray")
# footer_label.pack(side="bottom", pady=20)


# window.mainloop()

import tkinter as tk
from PIL import Image, ImageTk  # Pillow library required

# Create main window
root = tk.Tk()
root.title("Tkinter Background Image")
root.geometry("800x600")  # Set window size

# Load image (make sure it's resized to match window or use .place to stretch)
image = Image.open("login.png")  # Replace with your image path
bg_image = ImageTk.PhotoImage(image)

# Create a label to hold the background image
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)  # Stretch to cover entire window

# Add widgets on top
label = tk.Label(root, text="Hello World!", font=("Arial", 24), bg="white")
label.place(x=50, y=50)

bg_label.pack(side="bottom", fill="x")

# Run the app
root.mainloop()


