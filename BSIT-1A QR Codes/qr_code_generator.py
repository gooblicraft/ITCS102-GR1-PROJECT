import customtkinter as ctk
from customtkinter import *
import qrcode

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

window = ctk.CTk()
window.geometry("250x195")
window.title("QR CODE GENERATOR BY KYLA PINEDA")

def qr_code_ver1():
    student_id = ID_entry.get().strip()
    student_name = Name_entry.get().strip()
    student_age = age_entry.get().strip()
    if student_id and student_name:
        qr_data = f"Student ID: {student_id} Student Name: {student_name} Student Age: {student_age}"

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,)

        qr.add_data(qr_data)
        qr.make(fit=True)

        img = qr.make_image(fill="black", back_color="white")
        img.save(f"{student_name.replace(' ', '_')}.png")           #Soon to add specific directory for created qr codes -ed
        pop_up.configure(text = ("Generated Successfully"))
    else: 
        pop_up.configure(text = ("Failed to Generate, Missing a field."))
    print("QR Code Generated")
    
header = ctk.CTkLabel(window, text = "QR CODE", font = ("Arial", 15))
header.grid(row = 0, column = 2)
header.grid(row = 0, column = 2)
input_ID = ctk.CTkLabel(window, text = "School ID: ", font = ("Arial", 15))
input_ID.grid(row = 1, column = 1, pady = 5)
input_Name = ctk.CTkLabel(window, text = "Full Name: ", font = ("Arial", 15))
input_Name.grid(row = 2, column = 1, pady = 5)

ID_entry = ctk.CTkEntry(window)
ID_entry.grid(row = 1, column = 2, pady = 5)
Name_entry = ctk.CTkEntry(window)
Name_entry.grid(row = 2, column = 2, pady = 5)
age_entry = ctk.CTkEntry(window)
age_entry.grid(row = 3, column = 2, pady = 5)

Create_qr = ctk.CTkButton(window, width = 15, text = "Create Qr", command= qr_code_ver1)
Create_qr.grid(row = 3, column = 2, pady = 5)

pop_up = ctk.CTkLabel(window, text="")
pop_up.grid(row = 4, column = 2)

window.mainloop()