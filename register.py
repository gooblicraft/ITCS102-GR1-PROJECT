from tkinter import *
from PIL import Image

#Window kung saan dito magrergeister ang mga students para sa qr code
mainWindow = Tk()
mainWindow.geometry("400x400")
mainWindow.title("Attendance Fill Out Window")

Label(master =mainWindow, text="Event Attendance Log", font=("Helvetica", 24, "bold")).pack()
fNameEntry = Entry(master=mainWindow).pack()
mNameEntry = Entry(master=mainWindow).pack()
sNameEntry = Entry(master=mainWindow).pack()

# yearEntry = ComboBox(master=mainWindow, values=["1st", "2nd", "3rd", "4th"], state="readonly", corner_radius=10, width=90, height=30, border_color="Purple", button_color="Purple").pack()

# sectionEntry = CTkComboBox(master=mainWindow, values=["A", "B", "C", "D", "E"], state="readonly", corner_radius=10, width=90, height=30, border_color="Purple", button_color="Purple").pack()

# courseEntry = CTkComboBox(master=mainWindow, values=["BSIT", "BSA", "BTVTED", "BSSW", "DHRS", "ABELS", "BSBA", "BSPA"], state="readonly", corner_radius=10, width=90, height=30, border_color="Purple", button_color="Purple").pack()

Button(master=mainWindow, text="Register", height=30).pack()
mainWindow.mainloop()