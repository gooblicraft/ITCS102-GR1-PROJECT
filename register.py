from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# --- Main Window Setup ---
registerWindow = Tk()
registerWindow.geometry("639x639")
registerWindow.title("Attendance Fill Out Window")
registerWindow.iconbitmap('materials\\images\\icon.ico')
registerWindow.resizable(False, False)

# --- Background Image ---
bg_image = Image.open('materials\\images\\background.jpg')
bg_photo = ImageTk.PhotoImage(bg_image)

# --- Canvas for Background and Floating Text ---
canvas = Canvas(registerWindow, width=639, height=639, highlightthickness=0, bd=0)
canvas.pack(fill="both", expand=True)

# Place Background Image on Canvas
canvas.create_image(0, 0, anchor='nw', image=bg_photo)

# Create Floating Title Text
canvas.create_text(320, 50, text="Create Account", font=("Mokoto", 28, "bold"), fill="white")

# --- Transparent Entries ---
def create_transparent_entry(x, y, width=220, height=30):
    entry_bg = Entry(registerWindow, font=("Mokoto", 12), fg="white",
                        bg="#1a1a1a", bd=0, insertbackground="white",
                        highlightthickness=2, highlightbackground="#bb6ef1", highlightcolor="#bb6ef1")
    entry_bg.place(x=x, y=y, width=width, height=height)
    return entry_bg

# --- Transparent ComboBoxes ---
def create_transparent_combobox(values, x, y, width=90, height=30):
    var = StringVar()
    var.set(values[0])

    style = ttk.Style()
    style.configure("TCombobox",
                    fieldbackground="#1a1a1a",
                    background="#1a1a1a",
                    foreground="white",
                    borderwidth=0,
                    selectbackground="#1a1a1a",
                    selectforeground="white")

    combo = ttk.Combobox(registerWindow, textvariable=var, values=values, state="readonly", style="TCombobox")
    combo.place(x=x, y=y, width=width, height=height)
    return var

# --- Create all Entries ---
fNameEntry = create_transparent_entry(210, 100)
mNameEntry = create_transparent_entry(210, 150)
sNameEntry = create_transparent_entry(210, 200)

# --- Create ComboBoxes ---
yearVar = create_transparent_combobox(["1st", "2nd", "3rd", "4th"], 210, 250)
sectionVar = create_transparent_combobox(["A", "B", "C", "D", "E"], 310, 250)
courseVar = create_transparent_combobox(["BSIT", "BSA", "BTVTED", "BSSW", "DHRS", "ABELS", "BSBA", "BSPA"], 410, 250)

# --- Register Button ---
register_btn = Button(registerWindow, text="Register", font=("Mokoto", 14, "bold"),
                        fg="white", bg="#bb6ef1", activebackground="#a45de7",
                        activeforeground="white", borderwidth=0, relief="flat")
register_btn.place(x=210, y=320, width=220, height=40)

registerWindow.mainloop()
