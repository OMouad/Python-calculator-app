from tkinter import *

root = Tk()
root.title("My calculator")
entry = Entry(root, width=40, relief="flat",)
entry.grid(row=0, column=0, columnspan=4, padx=20, pady=20, ipadx=4, ipady=4)

key = ""


def button_comma():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current+".")


def button_changesign():
    button_first()
    entry.insert(0, f_num * -1)


def button_func(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current+number)


def button_clear():
    entry.delete(0, END)
    global f_num
    f_num = 0


def button_add():
    button_first()
    global key
    key = "add"


def button_minus():
    button_first()
    global key
    key = "minus"


def button_multiply():
    button_first()
    global key
    key = "multiply"


def button_divide():
    button_first()
    global key
    key = "divide"


def button_first():
    first = entry.get()
    global f_num
    if first == "":
        first = 0
    f_num = float(first)
    entry.delete(0, END)


def button_equal():
    second = entry.get()
    if second == "":
        second = 0
    entry.delete(0, END)
    if key == "add":
        entry.insert(0, f_num + float(second))
    elif key == "minus":
        entry.insert(0, f_num - float(second))
    elif key == "multiply":
        entry.insert(0, f_num * float(second))
    elif key == "divide":
        entry.insert(0, f_num / float(second))


# Creating buttons
button_1 = Button(root, text="1", width=10, pady=20, relief="flat",
                  command=lambda: button_func("1"))
button_2 = Button(root, text="2", width=10, pady=20, relief="flat",
                  command=lambda: button_func("2"))
button_3 = Button(root, text="3", width=10, pady=20, relief="flat",
                  command=lambda: button_func("3"))
button_4 = Button(root, text="4", width=10, pady=20, relief="flat",
                  command=lambda: button_func("4"))
button_5 = Button(root, text="5", width=10, pady=20, relief="flat",
                  command=lambda: button_func("5"))
button_6 = Button(root, text="6", width=10, pady=20, relief="flat",
                  command=lambda: button_func("6"))
button_7 = Button(root, text="7", width=10, pady=20, relief="flat",
                  command=lambda: button_func("7"))
button_8 = Button(root, text="8", width=10, pady=20, relief="flat",
                  command=lambda: button_func("8"))
button_9 = Button(root, text="9", width=10, pady=20, relief="flat",
                  command=lambda: button_func("9"))
button_0 = Button(root, text="0", width=10, pady=20, relief="flat",
                  command=lambda: button_func("0"))
button_plus = Button(root, text="+", width=10, pady=20, relief="flat",
                     command=button_add)
button_minus = Button(root, text="-", width=10, pady=20, relief="flat",
                      command=button_minus)
button_multiply = Button(root, text="X", width=10, relief="flat",
                         pady=20, command=button_multiply)
button_divide = Button(root, text="/", width=10, pady=20, relief="flat",
                       command=button_divide)
button_equal = Button(root, text="=", width=10, pady=52, relief="flat",
                      command=button_equal)
button_comma = Button(root, text=".", width=10, pady=20, relief="flat",
                      command=button_comma)
button_changesign = Button(root, text="+/-", width=10,
                           pady=20, relief="flat", command=button_changesign)
button_clear = Button(root, text="C", width=10, pady=20, relief="flat",
                      command=button_clear)

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
