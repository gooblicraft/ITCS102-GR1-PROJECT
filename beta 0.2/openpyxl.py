import os
from tkinter import *
from PIL import Image
from openpyxl import Workbook, load_workbook
from tkinter import messagebox

filename = "student_scores.xlsx"

def createExcel():
    if not os.path.exists(filename):
        wb = Workbook()
        ws = wb.active
        ws.append(["First Name", "Last Name", "Email", "Contact No.", "Nationality", "" ,"" ,"" ,""])
        wb.save(filename)

        
createExcel()


# <-----------------------------------------------------TKINTER------------------------------------------------->

mainWindow = Tk()
mainWindow.title("Try")
mainWindow.geometry("300x500")

mainWindow.mainloop()