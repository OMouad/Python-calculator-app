from tkinter import *
from math import *

root = Tk()
root.title("My calculator")

entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
entry.insert(0, '0.0')
