from tkinter import *

window = Tk()

window.geometry("665x640")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 640,
    width = 665,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(file="beta 0.3\\assets\\frame0\\button_1.png")
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=346.0,
    y=14.0,
    width=82.0,
    height=30.0
)

button_image_2 = PhotoImage(file="beta 0.3\\assets\\frame0\\button_2.png")
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=430.0,
    y=14.0,
    width=82.0,
    height=30.0
)

button_image_3 = PhotoImage(file="beta 0.3\\assets\\frame0\\button_3.png")
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=514.0,
    y=14.0,
    width=82.0,
    height=30.0
)

image_image_1 = PhotoImage(file="beta 0.3\\assets\\frame0\\image_1.png")
image_1 = canvas.create_image(
    175.0,
    87.0,
    image=image_image_1
)

image_image_2 = PhotoImage(file="beta 0.3\\assets\\frame0\\image_2.png")
image_2 = canvas.create_image(
    208.0,
    140.0,
    image=image_image_2
)

entry_image_1 = PhotoImage(file="beta 0.3\\assets\\frame0\\entry_1.png")
entry_bg_1 = canvas.create_image(
    88.5,
    318.0,
    image=entry_image_1
)
# Type (Facilitator or Attendee)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=46.0,
    y=312.0,
    width=85.0,
    height=10.0
)

button_image_4 = PhotoImage(file="beta 0.3\\assets\\frame0\\button_4.png")
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=487.0,
    y=565.0,
    width=106.0,
    height=38.0
)

image_image_3 = PhotoImage(file="beta 0.3\\assets\\frame0\\image_3.png")
image_3 = canvas.create_image(
    334.0,
    303.0,
    image=image_image_3
)

entry_image_2 = PhotoImage(file="beta 0.3\\assets\\frame0\\entry_2.png")
entry_bg_2 = canvas.create_image(
    87.5,
    292.5,
    image=entry_image_2
)
# Entry Name near at profile
entry_2 = Entry(
    bd=0,
    bg="#EEE9E9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=27.0,
    y=285.0,
    width=121.0,
    height=13.0
)

entry_image_3 = PhotoImage(file="beta 0.3\\assets\\frame0\\entry_3.png")
entry_bg_3 = canvas.create_image(
    298.5,
    252.5,
    image=entry_image_3
)
# Entry First Name
entry_3 = Entry(
    bd=0,
    bg="#EEE9E9",
    fg="#0E3269",
    font= ("JetBrains Mono", 10),
    highlightthickness=0
)
entry_3.place(
    x=203.0,
    y=245.0,
    width=191.0,
    height=13.0
)

entry_image_4 = PhotoImage(file="beta 0.3\\assets\\frame0\\entry_4.png")
entry_bg_4 = canvas.create_image(
    299.5,
    519.5,
    image=entry_image_4
)

# Entry Last Name
entry_4 = Entry(
    bd=0,
    bg="#EEE9E9",
    fg="#0E3269",
    font= ("JetBrains Mono", 10),
    highlightthickness=0
)
entry_4.place(
    x=204.0,
    y=512.0,
    width=191.0,
    height=13.0
)

entry_image_5 = PhotoImage(file="beta 0.3\\assets\\frame0\\entry_5.png")
entry_bg_5 = canvas.create_image(
    531.5,
    519.5,
    image=entry_image_5
)

# Entry Nationality
entry_5 = Entry(
    bd=0,
    bg="#EEE9E9",
    fg="#0E3269",
    font= ("JetBrains Mono", 10),
    highlightthickness=0
)
entry_5.place(
    x=436.0,
    y=512.0,
    width=191.0,
    height=13.0
)

entry_image_6 = PhotoImage(file="beta 0.3\\assets\\frame0\\entry_6.png")
entry_bg_6 = canvas.create_image(
    299.5,
    586.5,
    image=entry_image_6
)

# Entry Religion
entry_6 = Entry(
    bd=0,
    bg="#EEE9E9",
    fg="#0E3269",
    font= ("JetBrains Mono", 10),
    highlightthickness=0
)
entry_6.place(
    x=204.0,
    y=579.0,
    width=191.0,
    height=13.0
)

entry_image_7 = PhotoImage(file="beta 0.3\\assets\\frame0\\entry_7.png")
entry_bg_7 = canvas.create_image(
    524.5,
    252.5,
    image=entry_image_7
)

# Entry Age
entry_7 = Entry(
    bd=0,
    bg="#EEE9E9",
    fg="#0E3269",
    font= ("JetBrains Mono", 10),
    highlightthickness=0
)
entry_7.place(
    x=429.0,
    y=245.0,
    width=191.0,
    height=13.0
)

entry_image_8 = PhotoImage(file="beta 0.3\\assets\\frame0\\entry_8.png")
entry_bg_8 = canvas.create_image(
    268.0,
    316.5,
    image=entry_image_8
)

# Entry Sex
entry_8 = Entry(
    bd=0,
    bg="#EEE9E9",
    fg="#0E3269",
    font= ("JetBrains Mono", 10),
    highlightthickness=0
)
entry_8.place(
    x=201.0,
    y=309.0,
    width=134.0,
    height=13.0
)

entry_image_9 = PhotoImage(file="beta 0.3\\assets\\frame0\\entry_9.png")
entry_bg_9 = canvas.create_image(
    241.5,
    383.5,
    image=entry_image_9
)

# Entry Civil Status
entry_9 = Entry(
    bd=0,
    bg="#EEE9E9",
    fg="#0E3269",
    font= ("JetBrains Mono", 10),
    highlightthickness=0
)
entry_9.place(
    x=201.0,
    y=376.0,
    width=81.0,
    height=13.0
)

entry_image_10 = PhotoImage(file="beta 0.3\\assets\\frame0\\entry_10.png")
entry_bg_10 = canvas.create_image(
    386.0,
    383.5,
    image=entry_image_10
)
# Entry Disability
entry_10 = Entry(
    bd=0,
    bg="#EEE9E9",
    fg="#0E3269",
    font= ("JetBrains Mono", 10),
    highlightthickness=0
)
entry_10.place(
    x=333.0,
    y=376.0,
    width=106.0,
    height=13.0
)

entry_image_11 = PhotoImage(file="beta 0.3\\assets\\frame0\\entry_11.png")
entry_bg_11 = canvas.create_image(
    518.0,
    383.5,
    image=entry_image_11
)

# Entry Contact
entry_11 = Entry(
    bd=0,
    bg="#EEE9E9",
    fg="#0E3269",
    font= ("JetBrains Mono", 10),
    highlightthickness=0
)
entry_11.place(
    x=486.0,
    y=376.0,
    width=64.0,
    height=13.0
)

entry_image_12 = PhotoImage(file="beta 0.3\\assets\\frame0\\entry_12.png")
entry_bg_12 = canvas.create_image(
    435.5,
    316.5,
    image=entry_image_12
)
# Entry Email
entry_12 = Entry(
    bd=0,
    bg="#EEE9E9",
    fg="#0E3269",
    font= ("JetBrains Mono", 10),
    highlightthickness=0
)
entry_12.place(
    x=378.0,
    y=309.0,
    width=115.0,
    height=13.0
)

entry_image_13 = PhotoImage(file="beta 0.3\\assets\\frame0\\entry_13.png")
entry_bg_13 = canvas.create_image(
    571.5,
    314.5,
    image=entry_image_13
)
# Entry Permanent Password
entry_13 = Entry(
    bd=0,
    bg="#EEE9E9",
    fg="#0E3269",
    font= ("JetBrains Mono", 10),
    highlightthickness=0
)
entry_13.place(
    x=532.0,
    y=307.0,
    width=79.0,
    height=13.0
)
window.resizable(False, False)
window.mainloop()
