from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

window = Tk()

window.geometry("665x410")
window.configure(bg = "#FFFFFF")
window.title("Window 1")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 410,
    width = 665,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file="beta 0.1\\assets\\frame0\\button_1.png")
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=402.0,
    y=224.0,
    width=234.0,
    height=59.0
)

canvas.create_text(
    450.0,
    286.0,
    anchor="nw",
    text="Forgot Username/Password",
    fill="#757575",
    font=("JetBrains Mono", 10 * -1)
)

canvas.create_text(
    466.0,
    76.0,
    anchor="nw",
    text="Sign in your account",
    fill="#757575",
    font=("JetBrains Mono", 10 * -1)
)

canvas.create_text(
    419.0,
    38.0,
    anchor="nw",
    text="ScanTracker",
    fill="#060606",
    font= ("JetBrains Mono", 24, "bold")
)

image_image_1 = PhotoImage(
    file="beta 0.1\\assets\\frame0\\image_1.png")
image_1 = canvas.create_image(
    519.0,
    126.0,
    image=image_image_1
)

entry_1 = Entry(
    bd=0,
    bg="#AEAEAE",
    fg="#767676",
    highlightthickness=0,
    font= ("JetBrains Mono", 10, "bold")
)
entry_1.insert(0, "Student ID")
entry_1.place(
    x=464.0,
    y=118.0,
    width=152.0,
    height=14.0
)

image_image_2 = PhotoImage(
    file="beta 0.1\\assets\\frame0\\image_2.png")
image_2 = canvas.create_image(
    519.0,
    190.0,
    image=image_image_2
)

entry_2 = Entry(
    bd=0,
    bg="#AEAEAE",
    fg="#767676",
    highlightthickness=0,
    font= ("JetBrains Mono", 10, "bold")
)
entry_2.insert(0, "Password")
entry_2.place(
    x=464.0,
    y=182.0,
    width=152.0,
    height=14.0
)

button_image_2 = PhotoImage(
    file="beta 0.1\\assets\\frame0\\button_2.png")
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=402.0,
    y=325.0,
    width=234.0,
    height=57.0
)

image_image_3 = PhotoImage(
    file="beta 0.1\\assets\\frame0\\image_3.png")
image_3 = canvas.create_image(
    140.0,
    180.0,
    image=image_image_3
)
window.resizable(False, False)
window.mainloop()
