from tkinter import *
from tkinter import ttk

window = Tk()

window.geometry("665x640")
window.configure(bg = "#FFFFFF")

# =========== SECTION FOR STYLING TTK ==============

style = ttk.Style()
style.theme_use('default')

# Change the tab background color
bold_font = ("Helvetica", 10, "bold")
style.configure("TNotebook", background="#FFFFFF", borderwidth=0)
style.configure("TNotebook.Tab",
                background="#FFFFFF",
                foreground="#000000",
                padding=10,
                font=bold_font)

# Remove focus highlight (the dashed box)
style.layout("TNotebook.Tab",
            [('Notebook.tab', {'sticky': 'nswe', 'children':
                [('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children':
                    [('Notebook.label', {'side': 'top', 'sticky': ''})],
                })],
            })])

# Optional: active tab background
style.map("TNotebook.Tab",
        background=[("selected", "#0E3269")],
        foreground=[("selected", "#FFFFFF")])

# ============ SECTION FOR TABS ============

notebook = ttk.Notebook(window, style='TNotebook')
tab1 = Frame(notebook,bg="#FFFFFF", width=600, height=460)
tab2 = Frame(notebook)
tab3 = Frame(notebook)

notebook.add(tab1, text="Account tab")
notebook.add(tab2, text="Scan tab")
notebook.add(tab3, text="QR tab")
notebook.place(x=32, y=120)
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 640,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

# ========= SECTION FOR BUTTONS IN WINDOW =============




button_image_1 = PhotoImage(file="beta 0.4\\assets\\frame0\\button_1.png")
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

button_image_2 = PhotoImage(file="beta 0.4\\assets\\frame0\\button_2.png")
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

button_image_3 = PhotoImage(file="beta 0.4\\assets\\frame0\\button_3.png")
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

# ============ SECTION FOR IMAGES =============

image_image_1 = PhotoImage(file="beta 0.4\\assets\\frame0\\image_1.png")
image_1 = canvas.create_image(
    332.0,
    57.0,
    image=image_image_1
)
image_image_2 = PhotoImage(file="beta 0.4\\assets\\frame0\\image_2.png")
image_2 = Label(tab1, image=image_image_2)
image_2.place(

    x=10,
    y=1


)


window.resizable(False, False)
window.mainloop()
