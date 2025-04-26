from customtkinter import *

#Window kung saan dito magrergeister ang mga students para sa qr code

mainWindow = CTk()
mainWindow.geometry("400x400")

set_appearance_mode("dark")
set_default_color_theme("dark-blue")

CTkLabel(master =mainWindow, text="Event Attendance Log", font=("Helvetica", 24, "bold")).pack()
fNameEntry = CTkEntry(master=mainWindow, placeholder_text="First Name", corner_radius=10, border_color="Purple", width=220, height=30).pack()
mNameEntry = CTkEntry(master=mainWindow, placeholder_text="Middle Name", corner_radius=10, border_color="Purple", width=220, height=30).pack()
sNameEntry = CTkEntry(master=mainWindow, placeholder_text="Sur Name", corner_radius=10, border_color="Purple", width=220, height=30).pack()

yearEntry = CTkComboBox(master=mainWindow, values=["1st", "2nd", "3rd", "4th"], state="readonly", corner_radius=10, width=90, height=30, border_color="Purple", button_color="Purple").pack()

sectionEntry = CTkComboBox(master=mainWindow, values=["A", "B", "C", "D", "E"], state="readonly", corner_radius=10, width=90, height=30, border_color="Purple", button_color="Purple").pack()

courseEntry = CTkComboBox(master=mainWindow, values=["BSIT", "BSA", "BTVTED", "BSSW", "DHRS", "ABELS", "BSBA", "BSPA"], state="readonly", corner_radius=10, width=90, height=30, border_color="Purple", button_color="Purple").pack()

CTkButton(master=mainWindow, text="Register", width=220, height=30, fg_color="purple", corner_radius=10).pack()
mainWindow.mainloop()