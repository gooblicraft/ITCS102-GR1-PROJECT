from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

window = Tk()

window.geometry("665x410")
window.title("Window 1")
window.configure(bg = "#FFFFFF")


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
    file="assets\\frame0\\button_1.png")
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=408.0,
    y=245.0,
    width=234.0,
    height=59.0
)

canvas.create_text(
    449.0,
    307.0,
    anchor="nw",
    text="Forgot Username/Password",
    fill="#757575",
    font=("JetBrainsMono Bold", 10 * -1)
)

canvas.create_text(
    472.0,
    97.0,
    anchor="nw",
    text="Sign in your account",
    fill="#757575",
    font=("JetBrainsMono Bold", 10 * -1)
)

canvas.create_text(
    425.0,
    59.0,
    anchor="nw",
    text="ScanTracker",
    fill="#060606",
    font=("JetBrainsMono Bold", 32 * -1)
)

image_image_1 = PhotoImage(
    file="assets\\frame0\\image_1.png")
image_1 = canvas.create_image(
    525.0,
    147.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file="assets\\frame0\\entry_1.png")
entry_bg_1 = canvas.create_image(
    512.0,
    147.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#AEAEAE",
    fg="#767676",
    highlightthickness=0
)
entry_1.place(
    x=470.0,
    y=139.0,
    width=84.0,
    height=14.0
)

image_image_2 = PhotoImage(
    file="assets\\frame0\\image_2.png")
image_2 = canvas.create_image(
    525.0,
    211.0,
    image=image_image_2
)

entry_image_2 = PhotoImage(
    file="assets\\frame0\\entry_2.png")
entry_bg_2 = canvas.create_image(
    512.0,
    209.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#AEAEAE",
    fg="#767676",
    highlightthickness=0
)
entry_2.place(
    x=470.0,
    y=201.0,
    width=84.0,
    height=14.0
)

button_image_2 = PhotoImage(
    file="assets\\frame0\\button_2.png")
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=446.0,
    y=350.0,
    width=151.0,
    height=48.0
)

image_image_3 = PhotoImage(
    file="assets\\frame0\\image_3.png")
image_3 = canvas.create_image(
    160.0,
    180.0,
    image=image_image_3
)
window.resizable(False, False)
window.mainloop()
