from tkinter import *
from tkinter import ttk

# ================= FOR WINDOW 3 ====================
label_entry_pairs = []  # Each item: (label, entry, entry_place_args, label_place_args)

def create_label_entry_pair(tab, label_text, label_x, label_y, entry_x, entry_y, width=190, height=13,
                            bg="#EEE9E9", fg="#0E3269", font=("JetBrains Mono", 10)):

    label = Label(tab, text=label_text, bg="#EEE9E9", fg=fg, font=font)
    label.place(x=label_x, y=label_y)
    
    entry = Entry(tab, bg=bg, fg=fg, font=font, bd=0, highlightthickness=0)
    entry.place(x=entry_x, y=entry_y, width=width, height=height)
    entry.place_forget()

    entry_place_args = {"x": entry_x, "y": entry_y, "width": width, "height": height}
    label_place_args = {"x": label_x, "y": label_y}

    # Save both label + entry and their positions
    label_entry_pairs.append((label, entry, entry_place_args, label_place_args))


# editing = False

# def toggle_all():
#     global editing
#     if not editing:
#         for label, entry, entry_place_args, _ in label_entry_pairs:
#             entry.delete(0, END)
#             entry.insert(0, label['text'])
#             label.place_forget()
#             entry.place(**entry_place_args)
#         toggle_button.config(text="Save All")
#         editing = True
#     else:
#         for label, entry, _, label_place_args in label_entry_pairs:
#             label.config(text=entry.get())
#             entry.place_forget()
#             label.place(**label_place_args)
#         toggle_button.config(text="Edit All")
#         editing = False

# Toggle logic
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
tab3 = Frame(notebook, bg="#FFFFFF")
notebook.add(tab1, text="Account tab")
notebook.add(tab2, text="Scan tab")
notebook.add(tab3, text="QR tab")
notebook.place(x=32, y=120)

canvas = Canvas(tab1, bg="#FFFFFF", height=460, width=600, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

# ============ SECTION FOR IMAGES ============
image_image_1 = PhotoImage(file="beta 0.4/assets/frame0/image_1.png")
image_1 = Label(window, image=image_image_1, bg="white")
image_1.place(x=-2, y=2)

image_image_2 = PhotoImage(file="beta 0.4/assets/frame0/image_2.png")
image_2 = canvas.create_image(300, 230, image=image_image_2)

# ============ SECTION FOR IMAGE BUTTONS ============
button_image_1 = PhotoImage(file="beta 0.4/assets/frame0/button_1.png")
button_1 = Button(window, image=button_image_1, borderwidth=0, highlightthickness=0, command=lambda: print("button_1 clicked"), relief="flat")
button_1.place(x=346.0, y=14.0, width=82.0, height=30.0)

button_image_2 = PhotoImage(file="beta 0.4/assets/frame0/button_2.png")
button_2 = Button(window, image=button_image_2, borderwidth=0, highlightthickness=0, command=lambda: print("button_2 clicked"), relief="flat")
button_2.place(x=430.0, y=14.0, width=82.0, height=30.0)

button_image_3 = PhotoImage(file="beta 0.4/assets/frame0/button_3.png")
button_3 = Button(window, image=button_image_3, borderwidth=0, highlightthickness=0, command=lambda: print("button_3 clicked"), relief="flat")
button_3.place(x=514.0, y=14.0, width=82.0, height=30.0)

# Create label-entry fields with original styling and positions

# Each item: (What Tab?, entry_x, label x, label_y, entry_x, entry_y, width, height)
create_label_entry_pair(tab1, "John", 169, 70, 169, 88, 190, 13)
create_label_entry_pair(tab1, "Doe", 385, 70, 385, 88, 191, 13)
create_label_entry_pair(tab1, "Filipino", 170, 137, 170, 155, 129, 13)
create_label_entry_pair(tab1, "Catholic", 340, 137, 340, 155, 108, 13)
create_label_entry_pair(tab1, "25", 485, 137, 485, 155, 78, 13)
create_label_entry_pair(tab1, "Male", 169, 205, 169, 223, 78, 13)
create_label_entry_pair(tab1, "Single", 300, 205, 300, 223, 91, 13)
create_label_entry_pair(tab1, "None", 442, 205, 442, 223, 63, 13)
create_label_entry_pair(tab1, "09171234567", 172, 347, 172, 365, 186, 13)
create_label_entry_pair(tab1, "test@example.com", 392, 347, 392, 365, 188, 13)
create_label_entry_pair(tab1, "123 Street", 172, 417, 172, 435, 186, 13)

toggle_button = Button(tab1, text="Edit All", command=toggle_all)
toggle_button.place(x=500, y=10)

window.resizable(False, False)
window.mainloop()
