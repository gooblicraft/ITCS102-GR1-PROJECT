from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

main = Tk()
main.title("HABLOS MO AY RAMDAM PARIN SA DILIM")
main.geometry("960x540")
main.resizable(False,False)


bg_image = Image.open('BSIT-1A QR CODES/materials/images/background.png')

bg_photo = ImageTk.PhotoImage(bg_image)



# --- Canvas for Background and Floating Text ---
canvas = Canvas(main, width=639, height=639, highlightthickness=0, bd=0)
canvas.pack(fill="both", expand=True)

# Place Background Image on Canvas
canvas.create_image(0, 0, anchor='nw', image=bg_photo)


main.mainloop() 