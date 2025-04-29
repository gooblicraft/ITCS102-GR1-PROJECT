from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

main = Tk()
main.title("HABLOS MO AY RAMDAM PARIN SA DILIM")
main.geometry("960x540")
main.resizable(False,False)


bg_image = Image.open('ITCS102-GR1-PROJECT\Copy of design progress ver.2 (960 x 540 px).png')

bg_photo = ImageTk.PhotoImage(bg_image)



# --- Canvas for Background and Floating Text ---
canvas = Canvas(main, width=639, height=639, highlightthickness=0, bd=0)
canvas.pack(fill="both", expand=True)

# Place Background Image on Canvas
canvas.create_image(0, 0, anchor='nw', image=bg_photo)


# image = Button(main, image=)



# current_path = os.path.dirname(os.path.realpath("melanie-magdalena-VdFkSO3uePI-unsplash.jpg"))
# main.bg_image = customtkinter(Image.open(current_path + "melanie-magdalena-VdFkSO3uePI-unsplash.jpg"))



#images path (must be included to test)
# ImagePath2 = Image.open(r"C:\Users\admin\Desktop\CTK Project\Screenshot 2025-04-29 095120.png")
# ImageButton = CTkImage(light_image=ImagePath2,dark_image=ImagePath2,size=(100,50))



# bg = CTkImage(
#     light_image=Image.open(ImagePath),
#     dark_image=Image.open(ImagePath),
    
#     size=(960,540)
# )



# #label


# BgLabel = CTkLabel(master=main, image=bg,text="")
# BgLabel.place(x=0, y=0, relwidth=1, relheight=1)


# CTkLabel (master= main, text="hello",font=("Arial", 25), text_color="white",fg_color="transparent").place(x=100,y=100)
# # SearchBar = CTkEntry(master = main,placeholder_text="Search...", corner_radius=32).pack()x    




# def newindow():
#     print("Work In Progress")


# #button

# buttonimage = CTkButton(master=main,image=ImageButton, text="",command=newindow,hover_color="purple" ,bg_color="#581845",fg_color="transparent")
# buttonimage.place(x=435, y=462)




main.mainloop() 