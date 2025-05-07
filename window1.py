from tkinter import *
from tkinter import messagebox

# Show/Hide password logic via embedded button
password_visible = False

def toggle_password_button():
    global password_visible
    if entry_2.get() != "Password":
        if password_visible:
            entry_2.config(show="*")
            show_button.config(text="Show")
            password_visible = False
        else:
            entry_2.config(show="")
            show_button.config(text="Hide")
            password_visible = True
            
# Placeholder Handling Functions
def on_entry_click(entry, placeholder, is_password=False):
    if entry.get() == placeholder:
        entry.delete(0, "end")
        entry.config(fg="gray33")
        if is_password:
            if not password_visible:
                entry.config(show="*")
            else:
                entry.config(show="")

def on_focusout(entry, placeholder, is_password=False):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.config(fg="#767676")
        if is_password:
            entry.config(show="")


# Entry error for empty space
def entry_validation():
    student_id = entry_1.get().strip()
    password = entry_2.get().strip()

    if student_id == "" or student_id == "Student ID" or password == "" or password == "Password":
        messagebox.showerror("Input Error", "Please fill up all the boxes.")
    else:
        messagebox.showinfo("Great!", "You have successfully logged in to your account")
        new_window()



window = Tk()

window.geometry("665x410")
window.configure(bg="#FFFFFF")
window.title("Window 1")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=410,
    width=665,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# ================= IMAGES =================
image_image_1 = PhotoImage(
    file="assets\\window1\\image_1.png")
image_1 = canvas.create_image(
    519.0,
    126.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file="assets\\window1\\image_2.png")
image_2 = canvas.create_image(
    519.0,
    190.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file="assets\\window1\\image_3.png")
image_3 = canvas.create_image(
    140.0,
    180.0,
    image=image_image_3
)

# ================= LABEL TEXTS =================
canvas.create_text(
    450.0,
    286.0,
    anchor="nw",
    text="          Forgot Password?",
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
    font=("JetBrains Mono", 24, "bold")
)

# ================= ENTRY ==================
# Student ID Entry
entry_1 = Entry(
    bd=0,
    bg="#AEAEAE",
    fg="#767676",
    highlightthickness=0,
    font=("JetBrains Mono", 10, "bold")
)
entry_1.insert(0, "Student ID")
entry_1.place(
    x=464.0,
    y=118.0,
    width=152.0,
    height=14.0
)
# Bindings for Student ID
entry_1.bind("<FocusIn>", lambda event: on_entry_click(entry_1, "Student ID"))
entry_1.bind("<FocusOut>", lambda event: on_focusout(entry_1, "Student ID"))

# Password Entry
entry_2 = Entry(
    bd=0,
    bg="#AEAEAE",
    fg="#767676",
    highlightthickness=0,
    font=("JetBrains Mono", 10, "bold")
)
entry_2.insert(0, "Password")
entry_2.place(
    x=464.0,
    y=182.0,
    width=152.0,
    height=14.0
)
# Bindings for Password (with hiding)
entry_2.bind("<FocusIn>", lambda event: on_entry_click(entry_2, "Password", is_password=True))
entry_2.bind("<FocusOut>", lambda event: on_focusout(entry_2, "Password", is_password=True))


#New Window <<<<<<<<<<



# ================= BUTTONS ================

# Log in Submit Button
button_image_1 = PhotoImage(
    file="assets\\window1\\button_1.png")
button_logIn = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=entry_validation,
    relief="flat"
)
button_logIn.place(
    x=402.0,
    y=224.0,
    width=234.0,
    height=59.0
)

# Button inside the password entry area
show_button = Button(
    window,
    text="Show",
    command=toggle_password_button,
    font=("JetBrains Mono", 7),
    bd=0,
    bg="#AEAEAE",
    activebackground="#AEAEAE",
    fg="gray25",
    cursor="hand2"
)
show_button.place(x=568, y=180, width=40, height=18)

# Button Create Account
button_image_2 = PhotoImage(
    file="assets\\window1\\button_2.png")
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




#New window (log in page) <<<<<<<<<< 
def new_window():
    man = Tk()
    man.mainloop()



window.resizable(False, False)
window.mainloop()
