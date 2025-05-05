from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

window = Tk()
window.title("Window 2 Create Account")
window.geometry("665x410")
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
button_image_1 = PhotoImage(file="beta 0.2\\assets\\frame0\\button_1.png")
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=536.0,
    y=16.0,
    width=103.0,
    height=31.0
)

image_image_1 = PhotoImage(file="beta 0.2\\assets\\frame0\\image_1.png")
image_1 = canvas.create_image(
    444.0,
    33.0,
    image=image_image_1
)

image_image_2 = PhotoImage(file="beta 0.2\\assets\\frame0\\image_2.png")
image_2 = canvas.create_image(
    276.0,
    180.0,
    image=image_image_2
)

image_image_3 = PhotoImage(file="beta 0.2\\assets\\frame0\\image_3.png")
image_3 = canvas.create_image(
    285.0,
    295.0,
    image=image_image_3
)

image_image_4 = PhotoImage(file="beta 0.2\\assets\\frame0\\image_4.png")
image_4 = canvas.create_image(
    261.0,
    237.0,
    image=image_image_4
)

image_image_5 = PhotoImage(file="beta 0.2\\assets\\frame0\\image_5.png")
image_5 = canvas.create_image(
    485.0,
    180.0,
    image=image_image_5
)

image_image_6 = PhotoImage(file="beta 0.2\\assets\\frame0\\image_6.png")
image_6 = canvas.create_image(
    511.0,
    294.0,
    image=image_image_6
)

image_image_7 = PhotoImage(file="beta 0.2\\assets\\frame0\\image_7.png")
image_7 = canvas.create_image(
    569.0,
    237.0,
    image=image_image_7
)

canvas.create_text(
    76.0,
    22.0,
    anchor="nw",
    text="// Our Logo here",
    fill="#000716",
    font=("JetBrainsMono Bold", 12 * -1)
)

image_image_8 = PhotoImage(file="beta 0.2\\assets\\frame0\\image_8.png")
image_8 = canvas.create_image(
    39.0,
    33.0,
    image=image_image_8
)

image_image_9 = PhotoImage(file="beta 0.2\\assets\\frame0\\image_9.png")
image_9 = canvas.create_image(
    436.0,
    110.0,
    image=image_image_9
)

image_image_10 = PhotoImage(file="beta 0.2\\assets\\frame0\\image_10.png")
image_10 = canvas.create_image(
    333.0,
    203.0,
    image=image_image_10
)

image_image_11 = PhotoImage(file="beta 0.2\\assets\\frame0\\image_11.png")
image_11 = canvas.create_image(
    548.0,
    203.0,
    image=image_image_11
)

image_image_12 = PhotoImage(file="beta 0.2\\assets\\frame0\\image_12.png")
image_12 = canvas.create_image(
    333.0,
    317.0,
    image=image_image_12
)

button_image_2 = PhotoImage(file="beta 0.2\\assets\\frame0\\button_2.png")
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=251.0,
    y=346.0,
    width=177.0,
    height=45.0
)

image_image_13 =PhotoImage(file="beta 0.2\\assets\\frame0\\image_13.png")
image_13 = canvas.create_image(
    365.0,
    260.0,
    image=image_image_13
)

image_image_14 = PhotoImage(file="beta 0.2\\assets\\frame0\\image_14.png")
image_14 = canvas.create_image(
    548.0,
    317.0,
    image=image_image_14
)

image_image_15 = PhotoImage(file="beta 0.2\\assets\\frame0\\image_15.png")
image_15 = canvas.create_image(
    583.0,
    260.0,
    image=image_image_15
)

entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#767676",
    font= ("JetBrains Mono", 10 * -1),
    highlightthickness=0
)
entry_1.place(
    x=249.0,
    y=199.0,
    width=170.0,
    height=12.0
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#767676",
    font= ("JetBrains Mono", 10 * -1),
    highlightthickness=0
)
entry_2.place(
    x=466.0,
    y=198.0,
    width=170.0,
    height=12.0
)

entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#767676",
    font= ("JetBrains Mono", 10 * -1),
    highlightthickness=0
)
entry_4.place(
    x=249.0,
    y=312.0,
    width=170.0,
    height=12.0
)

entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#767676",
    font= ("JetBrains Mono", 10 * -1),
    highlightthickness=0
)
entry_5.place(
    x=464.0,
    y=312.0,
    width=170.0,
    height=12.0
)

button_image_3 = PhotoImage(file="beta 0.2\\assets\\frame0\\button_3.png")
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    border=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=450.0,
    y=346.0,
    width=177.0,
    height=45.0
)

image_image_16 = PhotoImage(file="beta 0.2\\assets\\frame0\\image_16.png")
image_16 = canvas.create_image(
    108.0,
    216.0,
    image=image_image_16
)
window.resizable(False, False)
window.mainloop()
