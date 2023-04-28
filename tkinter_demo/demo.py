from tkinter import *
from tkinter import ttk
import random

def clear_frame(frm):
    for widget in frm.winfo_children():
        widget.destroy()

def next_frame(title,frm):
    clear_frame(frm)
    title = "title " + str(random.randrange(100))
    btn_name = "click me " + str(random.randrange(100))
    ttk.Label(frm, text=title).grid(column=0, row=0)
    ttk.Button(frm, text=btn_name, command=lambda: next_frame("next", frm)).grid(column=1, row=0)


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
title = "title " + str(random.randrange(100))
next_frame(title,frm)
root.mainloop()