from openpyxl import load_workbook
from tkinter import *
from tkinter import ttk
import openpyxl
import os

accountID = None
accountType = None
firstName = None
lastName = None
email = None
contact_number = None
nationality = None
religion = None
sex = None
civil_status = None
age = None
isDisability = None
permanent_address = None
password = None

def load_account_data(account_id):
    global accountID, accountType, firstName, lastName, email, contact_number, nationality, religion, sex, civil_status, age, isDisability, permanent_address, password

    try:
        wb = load_workbook("AccountDatabase.xlsx")
        ws = wb.active

        headers = [cell.value for cell in ws[1]]

        for row in ws.iter_rows(min_row=2, values_only=True):
            current_id = str(row[0]).strip()
            if current_id == account_id:
                print(f"Details for Account ID: {account_id}")
                for header, value in zip(headers, row):
                    
                    if header == "ID Number":
                        accountID = value
                        print(f"Account ID: {accountID}")
                    elif header == "Account Type":
                        accountType = value
                        print(f"Account Type: {accountType}")
                    elif header == "First Name":
                        firstName = value
                        print(f"Account First Name: {firstName}")
                    elif header == "Last Name":
                        lastName = value
                        print(f"Account Last Name: {lastName}")
                    elif header == "Email":
                        email = value
                        print(f"Account Email: {email}")
                    elif header == "Contact Number":
                        contact_number = value
                        print(f"Contact Number: {contact_number}")
                    elif header == "Nationality":
                        nationality = value
                        print(f"Nationality : {nationality}")
                    elif header == "Religion":
                        religion = value
                        print(f"Religion : {religion}")
                    elif header == "Sex":
                        sex = value
                        print(f"Sex : {sex}")
                    elif header == "Civil Status":
                        civil_status = value
                        print(f"Civil Status : {civil_status}")
                    elif header == "Age":
                        age = value
                        print(f"Age : {age}")
                    elif header == "Disability":
                        isDisability = value
                        print(f"Disabillity : {isDisability}")
                    elif header == "Permanent Address":
                        permanent_address = value
                        print(f"Permanent Address : {permanent_address}")
                    elif header == "Password":
                        password = value
                        print(f"Password : {password}")
                    
                    # print(f"{header}: {value}")
                return accountID, accountType, firstName, lastName, email, contact_number, nationality, religion, sex, civil_status, age, isDisability, permanent_address, password

        print(f"Account ID {account_id} not found.")

    except FileNotFoundError:
        print("ERROR: AccountDatabase.xlsx not found.")

# Nakuha nayung account id, itutugma nalang sa account database then ishoshow dito yung code sa tab1
account_id = os.environ.get("ACCOUNT_ID")

if not account_id:
    print("ERROR: ACCOUNT_ID environment variable not set.")
else:
    load_account_data(account_id)
    print(f"Received Account ID: {account_id}")
    print(accountID, accountType, lastName, email, contact_number, nationality, religion, sex, civil_status, age, isDisability, permanent_address, password)

# ================= FOR WINDOW 3 ====================
label_entry_pairs = []  # Each item: (label, entry, entry_place_args, label_place_args)

def create_label_entry_pair(tab, label_text, label_x, label_y, entry_x, entry_y, width=190, height=13,
                            bg="#EEE9E9", fg="#0E3269", font=("JetBrains Mono", 10)):

    label = Label(tab, text=label_text, bg="#EEE9E9", fg=fg, font=font)
    label.place(x=label_x, y=label_y, width=width, height=height)
    
    entry = Entry(tab, bg=bg, fg=fg, font=font, bd=0, highlightthickness=0)
    entry.place(x=entry_x, y=entry_y, width=width, height=height)
    entry.place_forget()

    entry_place_args = {"x": entry_x, "y": entry_y, "width": width, "height": height}
    label_place_args = {"x": label_x, "y": label_y}

    # Save both label + entry and their positions
    label_entry_pairs.append((label, entry, entry_place_args, label_place_args))

editing = False

def toggle_all():
    global editing
    if not editing:
        # Switch from label → entry
        for label, entry, entry_place_args, _ in label_entry_pairs:
            entry.delete(0, END)
            entry.insert(0, label.cget("text"))  # pull label text
            label.place_forget()
            entry.place(**entry_place_args)
        toggle_button.config(text="Save All")
        editing = True
    else:
        # Switch from entry → label (with updated text)
        for label, entry, _, label_place_args in label_entry_pairs:
            updated_text = entry.get().strip()
            label.config(text=updated_text)  # set new label text
            entry.place_forget()
            label.place(**label_place_args)  # restore original label location
        toggle_button.config(text="Edit All")
        editing = False

window = Tk()
window.geometry("665x640")
window.configure(bg="#FFFFFF")

# =========== SECTION FOR STYLING TTK ==============
style = ttk.Style()
style.theme_use('default')
bold_font = ("JetBrains Mono", 10, "bold")
style.configure("TNotebook", background="#FFFFFF", borderwidth=0)
style.configure("TNotebook.Tab", background="#FFFFFF", foreground="#000000", padding=10, font=bold_font)
style.layout("TNotebook.Tab", [('Notebook.tab', {'sticky': 'nswe', 'children': [('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children': [('Notebook.label', {'side': 'top', 'sticky': ''})],})],})])
style.map("TNotebook.Tab", background=[("selected", "#0E3269")], foreground=[("selected", "#FFFFFF")])

# ============ SECTION FOR TABS ============
notebook = ttk.Notebook(window, style='TNotebook')
tab1 = Frame(notebook, bg="#FFFFFF", width=600, height=460)
tab2 = Frame(notebook, bg="#0E3269")
tab3 = Frame(notebook, bg="#0E3269")
tab4 = Frame(notebook, bg="#0E3269")
notebook.add(tab1, text="Account")
notebook.add(tab2, text="QR Scan")
notebook.add(tab3, text="QR Code")
notebook.add(tab4, text="Attendance")
notebook.place(x=32, y=120)

canvas = Canvas(tab1, bg="#FFFFFF", height=460, width=600, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

# ============ SECTION FOR IMAGES ============
image_image_1 = PhotoImage(file="assets/window3/account_tab/image_1.png")
image_1 = Label(window, image=image_image_1, bg="white")
image_1.place(x=-2, y=2)

image_image_2 = PhotoImage(file="assets/window3/account_tab/image_2.png")
image_2 = canvas.create_image(300, 230, image=image_image_2)

# ============ SECTION FOR IMAGE BUTTONS ============
button_image_1 = PhotoImage(file="assets/window3/account_tab/button_1.png")
button_1 = Button(window, image=button_image_1, borderwidth=0, highlightthickness=0, command=lambda: print("button_1 clicked"), relief="flat")
button_1.place(x=346.0, y=14.0, width=82.0, height=30.0)

button_image_2 = PhotoImage(file="assets/window3/account_tab/button_2.png")
button_2 = Button(window, image=button_image_2, borderwidth=0, highlightthickness=0, command=lambda: print("button_2 clicked"), relief="flat")
button_2.place(x=430.0, y=14.0, width=82.0, height=30.0)

button_image_3 = PhotoImage(file="assets/window3/account_tab/button_3.png")
button_3 = Button(window, image=button_image_3, borderwidth=0, highlightthickness=0, command=lambda: print("button_3 clicked"), relief="flat")
button_3.place(x=514.0, y=14.0, width=82.0, height=30.0)

# Create label-entry fields with original styling and positions

# Each item: (What Tab?, entry_x, label x, label_y, entry_x, entry_y, width, height)
create_label_entry_pair(tab1, firstName, 169, 85, 169, 88, 190, 13)
create_label_entry_pair(tab1, lastName, 385, 85, 385, 88, 191, 13)
create_label_entry_pair(tab1, nationality, 170, 148, 170, 153, 129, 13)
create_label_entry_pair(tab1, religion, 340, 147, 340, 155, 108, 13)
create_label_entry_pair(tab1, age, 485, 137, 485, 155, 78, 13)
create_label_entry_pair(tab1, sex, 169, 205, 169, 223, 78, 13)
create_label_entry_pair(tab1, civil_status, 300, 205, 300, 223, 91, 13)
create_label_entry_pair(tab1, isDisability, 442, 205, 442, 223, 63, 13)
create_label_entry_pair(tab1, contact_number, 172, 347, 172, 365, 186, 13)
create_label_entry_pair(tab1, email, 392, 347, 392, 365, 188, 13)
create_label_entry_pair(tab1, permanent_address, 172, 417, 172, 435, 186, 13)

toggle_button = Button(tab1, text="Edit All", command=toggle_all)
toggle_button.place(x=500, y=10)

window.resizable(False, False)
window.mainloop()
