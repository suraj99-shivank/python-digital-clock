import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")


def update_time():
    string = strftime("%H:%M:%S %p\n%D")
    label.config(text=string)
    label.after(1000, update_time)


label = tk.Label(root, font=("ds-digital", 80),
                 background="black", foreground="cyan")
label.pack(anchor="center")

update_time()
root.mainloop()
