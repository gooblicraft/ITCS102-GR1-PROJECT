from tkinter import *
from tkinter import messagebox
from openpyxl import Workbook, load_workbook

file_path = "AccountDatabase.xlsx"
def load_credentials(path):
    wb = load_workbook(path)
    ws = wb.active
    
    return {row[0]: row[1] for row in ws.iter_rows(min_row=2, values_only=True)}

credentials = load_credentials(file_path)

def validate_login():
    input_username = username_entry.get().strip()
    input_password = password_entry.get().strip()

    try:
        wb = load_workbook("AccountDatabase.xlsx")
        ws = wb.active

        for row in ws.iter_rows(min_row=2, values_only=True):
            first_name = str(row[2]).strip().lower() if row[2] else ""
            last_name = str(row[3]).strip().lower() if row[3] else ""
            password = str(row[-1]).strip() if len(row) > -1 and row[-1] else ""

            full_name = f"{first_name} {last_name}".strip() 
            
            # debugging
            # print(f"Checking: '{full_name}' with password '{password}'")

            if input_username == full_name and input_password == password:
                messagebox.showinfo("Login", f"Welcome, {first_name.capitalize()}!")
                window.destroy()
                return

        messagebox.showerror("Login Failed", "Invalid username or password.")

    except FileNotFoundError:
        messagebox.showerror("File Error", "The file 'AccountDatabase.xlsx' was not found.")


# Show/Hide password logic via embedded button
password_visible = False
def toggle_password_button():
    global password_visible
    if password_entry.get() != "Password":
        if password_visible:
            password_entry.config(show="*")
            show_button.config(text="Show")
            password_visible = False
        else:
            password_entry.config(show="")
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
    student_id = username_entry.get().strip()
    password = password_entry.get().strip()

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
username_entry = Entry(
    bd=0,
    bg="#AEAEAE",
    fg="#767676",
    highlightthickness=0,
    font=("JetBrains Mono", 10, "bold")
)
username_entry.insert(0, "Student ID")
username_entry.place(
    x=464.0,
    y=118.0,
    width=152.0,
    height=14.0
)
# Bindings for Student ID
username_entry.bind("<FocusIn>", lambda event: on_entry_click(username_entry, "Student ID"))
username_entry.bind("<FocusOut>", lambda event: on_focusout(username_entry, "Student ID"))

# Password Entry
password_entry = Entry(
    bd=0,
    bg="#AEAEAE",
    fg="#767676",
    highlightthickness=0,
    font=("JetBrains Mono", 10, "bold")
)
password_entry.insert(0, "Password")
password_entry.place(
    x=464.0,
    y=182.0,
    width=152.0,
    height=14.0
)
# Bindings for Password (with hiding)
password_entry.bind("<FocusIn>", lambda event: on_entry_click(password_entry, "Password", is_password=True))
password_entry.bind("<FocusOut>", lambda event: on_focusout(password_entry, "Password", is_password=True))


#New Window <<<<<<<<<<



# ================= BUTTONS ================

# Log in Submit Button
button_image_1 = PhotoImage(
    file="assets\\window1\\button_1.png")
button_logIn = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=validate_login,
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
