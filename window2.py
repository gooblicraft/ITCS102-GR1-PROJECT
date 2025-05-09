from tkinter import *
from tkinter import messagebox, filedialog
from tkinter import ttk
from openpyxl import *
from openpyxl import styles
from openpyxl import utils 
import qrcode , os, re, subprocess, random
from PIL import Image, ImageTk

account_set = None
def in_facilitator():
    global account_set
    account_set = "Facilitator"
    createExcel()
    submit_data()
    return account_set

def in_attendee():
    global account_set
    account_set = "Attendee"
    createExcel() 
    submit_data()
    return account_set

def login():
    subprocess.Popen(['python', 'window1.py'])
    window.destroy()

#<===================================================== OPENPYXL===================================================>


filename = "AccountDatabase.xlsx"

def createExcel():
    if not os.path.exists(filename):
        workbook = Workbook()
        ws = workbook.active
        ws.append(["ID Number","Account Type","First Name", "Last Name", 
                "Email","Contact Number", "Nationality", "Religion", 
                "Sex", "Civil Status", "Age", "Disability", "Permanent Address","Password"])  
        workbook.save(filename)

def generate_qr_code(data, last_name):
    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")],
        title="Save QR Code As",
        initialfile=f"{last_name.replace(' ', '_')}_qr"
    )

    if not save_path:
        return None  

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(save_path)

    return save_path  

def submit_data():
    path = filename  
    workbook = load_workbook(path)
    sheet = workbook.active

    account_id = str(random.randint(10**5, 10**6 - 1))
    account_type = account_set  
    first_name = Fname_entry.get()
    last_name = Lname_entry.get()
    email = email_entry.get().strip()
    contact_num = contact_entry.get()
    nationality = nationality_entry.get()
    religion = cb_religion.get()
    sex = cb_sex.get()
    civil_status = cb_civil_status.get()
    age = age_entry.get()
    disability = disability_RB.get()
    permanent_address = address_entry.get()
    password = real_pass  
    
# ===================================================== User Restrictions ====================================================================
    
    # First Name
    if not first_name:
        messagebox.showerror("Invalid First Name", "Please enter your first name.")
        return
    
    if len(first_name) < 2 or not re.match(r"^[A-Za-z\s]+$", first_name):
        messagebox.showerror("Invalid Input", "First Name must be at least 2 letters and can only contain letters.")
        return
    
    # Last Name
    if not last_name:
        messagebox.showerror("Invalid Last Name", "Please enter your last name.")
        return
    
    if len(last_name) < 2 or not re.match(r"^[A-Za-z\s]+$", last_name):
        messagebox.showerror("Invalid Input", "Last Name must be at least 2 letters and can only contain letters.")
        return
    
    # Email
    if not email:
        messagebox.showerror("Invalid Email", "Please enter your email address.")
        return

    if not re.match(r"^[a-zA-Z0-9._%+-]+@gmail\.com$", email):
        messagebox.showerror("Invalid Input", "Please enter a valid email address. (user@example.com).")
        return

    # Contact Number
    if not contact_num:
        messagebox.showerror("Invalid Contact Number", "Please enter your contact number.")
        return
    
    if len(contact_num) != 11:
        messagebox.showerror("Invalid Input", "Contact number must be exactly 11 digits.")
        return
    
    # Nationality
    if not nationality:
        messagebox.showerror("Invalid Nationality", "Please input your nationality to proceed.")
        return
    
    if len(nationality) < 4 or not re.match(r"^[A-Za-z\s]+$", nationality):
        messagebox.showerror("Invalid Input", "Nationality must be at least 4 letters and can only contain letters.")
        return
    
    # Religion
    if religion == "Select":
        messagebox.showerror("Invalid Religion", "Please input your religion to proceed.")
        return
    
    # Sex
    if sex == "Select":
        messagebox.showerror("Invalid Sex", "Please input your sex to proceed.")
        return
    
    # Civil Status
    if civil_status == "Select":
        messagebox.showerror("Invalid Civil Status", "Please input your civil status to proceed.")
        return
    
    # Age entry
    age_string = age_entry.get()
    if not age_string.isdigit():
        messagebox.showerror("Input Error", "Please enter a valid age.")
        return

    age = int(age_string)

    
    # Civil Status & Age
    if civil_status == "Married" and age <= 17:
        messagebox.showerror("Invalid Input", "You must be 18 and about to get married.")
        return
    
    # Disability
    if disability == "null":
        messagebox.showerror("Invalid Input", "Please validate if you're a disabled person or not.")
        return
    
    # Permanent Address
    if not permanent_address:
        messagebox.showerror("Invalid Permanent Address", "Please enter your permanent address.")
        return
    
    if len(permanent_address) < 10:
        messagebox.showerror("Invalid Address", "Please input a valid permanent address.")
        return

    # Password
    pass1 = confirm_pass.get()
    pass2 = set_pass.get()

    if not pass1 or not pass2:
        messagebox.showerror("Invalid Password", "Both password fields are required.")
        return

    if pass1 != pass2:
        messagebox.showerror("Password Mismatch", "Passwords do not match.")
        return
    
    if len(pass1) < 8 or len(pass2) < 8:
        messagebox.showerror("Invalid Password", "Password must be at least 8 characters long.")
        return

    password = pass1

    
    required_fields = [
        account_id, account_type, first_name, last_name, email,
        contact_num, nationality, religion, sex, civil_status,
        age, disability, permanent_address, password
    ]

    if all(required_fields):
        row_values = required_fields
        sheet.append(row_values)
        workbook.save(path)

        data = {
            "ID Number": account_id,
            "Account Type": account_type,
            "First Name": first_name,
            "Last Name": last_name,
            "Email": email,
            "Contact Number": contact_num,
            "Nationality": nationality,
            "Religion": religion,
            "Sex": sex,
            "Civil Status": civil_status,
            "Age": age,
            "Disability": disability,
            "Permanent Address": permanent_address,
            "Password": password
        }

        qr_data = "\n".join([f"{key}: {value}" for key, value in data.items()])
        qr_path = generate_qr_code(qr_data, last_name)

        if qr_path:
            window.withdraw()
            topWindow = Toplevel()
            topWindow.geometry("350x350")
            topWindow.iconbitmap("assets\\logo.ico")
            topWindow.resizable(False,False)
            topWindow.title("QR Code")

            img = Image.open(qr_path)
            img = img.resize((230, 230))
            photo = ImageTk.PhotoImage(img)

            successful_label =Label(topWindow, text="Signed Up Successfully!\n Account and QR Code generated.", font=("JetBrainsMono Bold", 12))
            successful_label.pack(pady=10)
            
            qr_label = Label(topWindow, image=photo)
            qr_label.image = photo  
            qr_label.pack(pady=10)
            
            proceed_button = Button(topWindow, text="Proceed", command=login)
            proceed_button.pack()
            
            return False

        else:
            messagebox.showwarning("Cancelled", "QR Code was not saved.")
    else:
        messagebox.showerror("Error", "Please fill in all fields before submitting.")

real_pass = None

window = Tk()
window.title("Window 2 Create Account")
window.iconbitmap("assets\\logo.ico")
window.geometry("670x590")
window.configure(bg = "#FFFFFF")

# Styling ttk 
style = ttk.Style()
style.theme_use('clam')

# Define custom layout without border
style.layout('Custom.TCombobox',
            [('Combobox.downarrow', {'side': 'right', 'sticky': ''}),
            ('Combobox.padding', {'expand': '1', 'sticky': 'nswe',
            'children': [('Combobox.textarea', {'sticky': 'nswe'})]})])

# Configure background and remove border
style.configure('Custom.TCombobox',
                fieldbackground='#ffffff',  # Entry field background
                background='#ffffff',       # Dropdown background
                borderwidth=0,
                relief='flat',
                padding=0)

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 590,
    width = 665,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge", 
    scrollregion=(0, 0, 670, 550)
)

canvas.place(x = 0, y = 0)
# y_scroll = Scrollbar(window, orient="vertical", command=canvas.yview)
# canvas.config(yscrollcommand=y_scroll.set)
# y_scroll.place(x=651, y=0, height=410)



# ======== IMAGES =========

image_image_1 = PhotoImage(file="assets\\window2\\image_1.png")
image_1 = canvas.create_image(
    444.0,
    33.0,
    image=image_image_1
)

image_image_2 = PhotoImage(file="assets\\Window2(new)\\First_name.png")
image_2 = canvas.create_image(
    276.0,
    180.0,
    image=image_image_2
)

image_image_4 = PhotoImage(file="assets\\Window2(new)\\EMAIL (2).png")
image_4 = canvas.create_image(
    261.0,
    237.0,
    image=image_image_4
)

image_image_5 = PhotoImage(file="assets\\Window2(new)\\Last_name.png")
image_5 = canvas.create_image(
    485.0,
    180.0,
    image=image_image_5
)

image_image_7 = PhotoImage(file="assets\\window2\\image_7.png")
image_7 = canvas.create_image(
    538.0,
    237.0,
    image=image_image_7
)

image_image_8 = PhotoImage(file="assets\\window2\\image_8.png")
image_8 = canvas.create_image(
    99.0,
    33.0,
    image=image_image_8
)

image_image_9 = PhotoImage(file="assets\\window2\\image_9.png")
image_9 = canvas.create_image(
    436.0,
    110.0,
    image=image_image_9
)
# Image Entry FIRST NAME
image_image_10 = PhotoImage(file="assets\\Window2(new)\\lastName.png")
image_10 = canvas.create_image(
    333.0,
    203.0,
    image=image_image_10
)

image_image_11 = PhotoImage(file="assets\\Window2(new)\\lastName.png")
image_11 = canvas.create_image(
    548.0,
    203.0,
    image=image_image_11
)

# ========  Set Password ========= 
# Entry set password
image_image_3 = PhotoImage(file="assets\\window2\\image_3.png")
image_3 = canvas.create_image(
    280.0,
    450.0,
    image=image_image_3
)
image_image_12 = PhotoImage(file="assets\\Window2(new)\\SetPass.png")

# image entry SET PASSWORD
image_12 = canvas.create_image(
    330.0,
    470.0,
    image=image_image_12
)

# ============ Confirm password ===========

# image confirm password
image_image_6 = PhotoImage(file="assets\\Window2\\image_6.png")
image_6 = canvas.create_image(
    500.0,
    450.0,
    image=image_image_6
)

# Border confirm password
image_image_14 = PhotoImage(file="assets\\Window2(new)\\ConfirmPass.png")
image_14 = canvas.create_image(
    540.0,
    470.0,
    image=image_image_14
)
image_image_18 = PhotoImage(file="assets\\window2\\image_18.png")
image_18 = canvas.create_image(
    128.0,
    456.0,
    image=image_image_18
)
# ======== Whole Mid code =====
# Image MID
image_image_17 = PhotoImage(file="assets\\Window2(new)\\Middle.png")
image_17 = canvas.create_image(
    434.0,
    360.0,
    image=image_image_17
)

# ==================== COMBOBOX AND RADIO BUTTON =========================

# Combobox religion
cb_religion = ttk.Combobox(values=["Catholic", "INC", "Muslim"], style='Custom.TCombobox', width=25, state="readonly")
cb_religion.set("Select")
canvas.create_window(540, 316, window=cb_religion)

# Combobox Sex
cb_sex = ttk.Combobox(values=["Male", "Female"], style='Custom.TCombobox', width=20, state="readonly")
cb_sex.set("Select")
canvas.create_window(310, 370, window=cb_sex)

# Combobox Civil Satus
cb_civil_status = ttk.Combobox(values=["Single", "Married"], style='Custom.TCombobox', width=20, state="readonly")
cb_civil_status.set("Select")
canvas.create_window(470, 370, window=cb_civil_status)

# Disability Radio Button
disability_RB = StringVar()
disability_RB.set("null")
rb_yes_disable = Radiobutton(
    window, 
    text="yes", 
    variable=disability_RB, 
    value="yes",
    bg="#ffffff", 
    activebackground="#ffffff", 
    highlightthickness=0, 
    bd=0)
canvas.create_window(250, 422, window=rb_yes_disable)

rb_no_disable = Radiobutton(
    window, 
    text="no", 
    variable=disability_RB, 
    value="no",
    bg="#ffffff", 
    activebackground="#ffffff",
    highlightthickness=0, 
    bd=0)
canvas.create_window(300, 422, window=rb_no_disable)

# ====================== ENTRY ======================

def limit_length(new_text):
    return len(new_text) <= 8

charmax = (window.register(limit_length), '%P')


# First Name entry
Fname_entry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#767676",
    font= ("JetBrains Mono", 10 * -1),
    highlightthickness=0
)
canvas.create_window(334, 205, window=Fname_entry, width=165, height=12)

# Lastname entry
Lname_entry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#767676",
    font= ("JetBrains Mono", 10 * -1),
    highlightthickness=0
)
canvas.create_window(551, 204, window=Lname_entry, width=165, height=12)

# Email Entry
email_entry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#767676",
    font= ("JetBrains Mono", 10 * -1),
    highlightthickness=0
)
canvas.create_window(350, 260, window=email_entry, width=212, height=12)

# Contact Number entry
def limited_numbers(new_char, full_text_after):
    return new_char.isdigit() and len(full_text_after) <= 11

limited_num = window.register(limited_numbers)

contact_entry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#767676",
    font= ("JetBrains Mono", 10 * -1),
    highlightthickness=0,
    validate="key",
    validatecommand=(limited_num , "%S", "%P")
)
canvas.create_window(570, 260, window=contact_entry, width=122, height=12)

# Entry nationality
address_entry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#767676",
    font= ("JetBrains Mono", 10 * -1),
    highlightthickness=0
)
canvas.create_window(480, 422, window=address_entry, width=276, height=12)

# Age Entry
def limit_age(new_char, full_text_after):
    return new_char.isdigit() and len(full_text_after) <= 3

limited_age = window.register(limit_age)

age_entry = Entry(
    window,
    bd=0,
    bg="#FFFFFF",
    fg="#767676",
    font=("JetBrains Mono", 10 * -1),
    highlightthickness=0,
    validate="key",
    validatecommand=(limited_age, "%S", "%P")  
)
canvas.create_window(595, 370, window=age_entry, width=60, height=12)


# Entry nationality
nationality_entry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#767676",
    font= ("JetBrains Mono", 10 * -1),
    highlightthickness=0
)
canvas.create_window(325, 316, window=nationality_entry, width=160, height=12)

# entry confirm password
confirm_pass = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#767676",
    font= ("JetBrains Mono", 10 * -1),
    highlightthickness=0,
    validate='key',
    validatecommand=charmax
)
canvas.create_window(540, 470, window=confirm_pass, width=165, height=12)

# entry SET PASSOWRD
set_pass= Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#767676",
    font= ("JetBrains Mono", 10 * -1),
    highlightthickness=0,
    validate='key',
    validatecommand=charmax
)
canvas.create_window(330, 470, window=set_pass, width=165, height=12)

image_image_16 = PhotoImage(file="assets\\window2\\image_16.png")
image_16 = canvas.create_image(
    108.0,
    216.0,
    image=image_image_16
)

# ============== BUTTONS ===============

# Button Facilitator
button_image_2 = PhotoImage(file="assets\\window2\\button_2.png")
button_facilitator = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command= in_facilitator,
    relief="flat"
)
canvas.create_window(330, 520, window=button_facilitator, width=177, height=45)


# Button Attendee
button_image_3 = PhotoImage(file="assets\\window2\\button_3.png")
button_attendee = Button(
    image=button_image_3,
    borderwidth=0,
    border=0,
    highlightthickness=0,
    command= in_attendee,
    relief="flat"
)
canvas.create_window(540, 520, window=button_attendee, width=177, height=45)

# Button log im
button_image_1 = PhotoImage(file="assets\\window2\\button_1.png")
button_logIn = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=login,
    relief="flat"
)
canvas.create_window(595, 32, window=button_logIn, width=103, height=31)

image_image_13 =PhotoImage(file="assets\\Window2(new)\\Email.png")
image_13 = canvas.create_image(
    352.0,
    260.0,
    image=image_image_13
)

image_image_15 = PhotoImage(file="assets\\Window2(new)\\ContactNo.png")
image_15 = canvas.create_image(
    570.0,
    263.0,
    image=image_image_15
)


window.resizable(False, False)
window.mainloop()