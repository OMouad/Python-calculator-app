from tkinter import *
from math import *

root = Tk()
root.title("My calculator")

entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
entry.insert(0, '0.0')


def button_func():
    return


button_1 = Button(root, text="1", padx=10, pady=20, command=button_func)
button_2 = Button(root, text="2", padx=10, pady=20, command=button_func)
button_3 = Button(root, text="3", padx=10, pady=20, command=button_func)
button_4 = Button(root, text="4", padx=10, pady=20, command=button_func)
button_5 = Button(root, text="5", padx=10, pady=20, command=button_func)
button_6 = Button(root, text="6", padx=10, pady=20, command=button_func)
button_7 = Button(root, text="7", padx=10, pady=20, command=button_func)
button_8 = Button(root, text="8", padx=10, pady=20, command=button_func)
button_9 = Button(root, text="9", padx=10, pady=20, command=button_func)
button_0 = Button(root, text="0", padx=10, pady=20, command=button_func)

root.mainloop()
