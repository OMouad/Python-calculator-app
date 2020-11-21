from tkinter import *
from math import *

root = Tk()
root.title("My calculator")

entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
entry.insert(0, '0.0')


def button_func():
    return


# Creating buttons
button_1 = Button(root, text="1", width=10, pady=20, command=button_func)
button_2 = Button(root, text="2", width=10, pady=20, command=button_func)
button_3 = Button(root, text="3", width=10, pady=20, command=button_func)
button_4 = Button(root, text="4", width=10, pady=20, command=button_func)
button_5 = Button(root, text="5", width=10, pady=20, command=button_func)
button_6 = Button(root, text="6", width=10, pady=20, command=button_func)
button_7 = Button(root, text="7", width=10, pady=20, command=button_func)
button_8 = Button(root, text="8", width=10, pady=20, command=button_func)
button_9 = Button(root, text="9", width=10, pady=20, command=button_func)
button_0 = Button(root, text="0", width=10, pady=20, command=button_func)
button_plus = Button(root, text="+", width=10, pady=20, command=button_func)
button_minus = Button(root, text="-", width=10, pady=20, command=button_func)
button_multiply = Button(root, text="*", width=10,
                         pady=20, command=button_func)
button_divide = Button(root, text="/", width=10, pady=20, command=button_func)
button_equal = Button(root, text="=", width=10, pady=52, command=button_func)
button_comma = Button(root, text=".", width=10, pady=20, command=button_func)
button_changesign = Button(root, text="+/-", width=10,
                           pady=20, command=button_func)
button_clear = Button(root, text="C", width=10, pady=20, command=button_func)

# Displaying buttons
button_0.grid(row=5, column=1)
button_comma.grid(row=5, column=2)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_equal.grid(row=4, column=3, rowspan=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_plus.grid(row=3, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_minus.grid(row=2, column=3)

button_clear.grid(row=1, column=0)
button_changesign.grid(row=1, column=1)
button_divide.grid(row=1, column=2)
button_multiply.grid(row=1, column=3)

root.mainloop()
