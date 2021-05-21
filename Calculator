from tkinter import *
canvas = Tk()
canvas.title("Calculator")
canvas.geometry("450x340")
inp = Entry(canvas, width=45)
inp.grid(row=0, column=0, columnspan=50)


def click(number):
    current = inp.get()
    inp.delete(0, END)
    inp.insert(0, current + str(number))


def clear():
    inp.delete(0, END)


def add():
    first_num = inp.get()
    global f_num
    global op
    op = "addition"
    f_num = int(first_num)
    inp.delete(0, END)


def sub():
    first_num = inp.get()
    global f_num
    global op
    op = "subtraction"
    f_num = int(first_num)
    inp.delete(0, END)


def multi():
    first_num = inp.get()
    global f_num
    global op
    op = "multiplication"
    f_num = int(first_num)
    inp.delete(0, END)


def div():
    first_num = inp.get()
    global f_num
    global op
    op = "division"
    f_num = int(first_num)
    inp.delete(0, END)


def equal():
    second_num = inp.get()
    inp.delete(0, END)
    if op == "addition":
        inp.insert(0, f_num + int(second_num))
    elif op == "subtraction":
        inp.insert(0, f_num - int(second_num))
    elif op == "multiplication":
        inp.insert(0, f_num * int(second_num))
    elif op == "division":
        inp.insert(0, f_num / int(second_num))


button_clear = Button(canvas, text="Clear", padx=40, pady=20, command=clear)
button_clear.grid(row=5, column=3)
button = Button(canvas, text="1", padx=40, pady=20, command=lambda: click(1))
button.grid(row=1, column=0)
button_2 = Button(canvas, text="2", padx=40, pady=20, command=lambda: click(2))
button_2.grid(row=1, column=1)
button_3 = Button(canvas, text="3", padx=40, pady=20, command=lambda: click(3))
button_3.grid(row=1, column=2)
button_4 = Button(canvas, text="4", padx=40, pady=20, command=lambda: click(4))
button_4.grid(row=2, column=0)
button_5 = Button(canvas, text="5", padx=40, pady=20, command=lambda: click(5))
button_5.grid(row=2, column=1)
button_6 = Button(canvas, text="6", padx=40, pady=20, command=lambda: click(6))
button_6.grid(row=2, column=2)
button_7 = Button(canvas, text="7", padx=40, pady=20, command=lambda: click(7))
button_7.grid(row=3, column=0)
button_8 = Button(canvas, text="8", padx=40, pady=20, command=lambda: click(8))
button_8.grid(row=3, column=1)
button_9 = Button(canvas, text="9", padx=40, pady=20, command=lambda: click(9))
button_9.grid(row=3, column=2)
button_0 = Button(canvas, text="0", padx=40, pady=20, command=lambda: click(0))
button_0.grid(row=4, column=0)
button_add = Button(canvas, text="+", padx=40, pady=20, command=add)
button_add.grid(row=4, column=1)
button_sub = Button(canvas, text="-", padx=40, pady=20, command=sub)
button_sub.grid(row=4, column=2)
button_multi = Button(canvas, text="*", padx=40, pady=20, command=multi)
button_multi.grid(row=5, column=0)
button_div = Button(canvas, text="/", padx=40, pady=20, command=div)
button_div.grid(row=5, column=1)
button_equal = Button(canvas, text="=", padx=40, pady=20, command=equal)
button_equal.grid(row=5, column=2)
canvas.mainloop()
