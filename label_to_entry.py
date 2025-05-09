import tkinter as tk

def switch_to_entry():
    label.pack_forget()
    entry.delete(0, tk.END)
    entry.insert(0, label['text'])
    entry.pack()
    button.config(text="Save", command=switch_to_label)

def switch_to_label():
    entry.pack_forget()
    label.config(text=entry.get())
    label.pack()
    button.config(text="Edit", command=switch_to_entry)

root = tk.Tk()
root.title("Label to Entry Toggle")

# Initial label
label = tk.Label(root, text="Click Edit to modify me")
label.pack()

# Entry widget, hidden initially
entry = tk.Entry(root)

# Button to toggle between Edit and Save
button = tk.Button(root, text="Edit", command=switch_to_entry)
button.pack()

root.mainloop()
