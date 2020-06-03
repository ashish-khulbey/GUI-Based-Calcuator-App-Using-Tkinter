from tkinter import *

root = Tk()
root.title("Calculator+-*/")

e = Entry(root, width=30, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=40, pady=50)


def button_click(clicked):
    e.insert(END, clicked)


def ans():
    temp_str = e.get()
    e.delete(0, END)
    e.insert(0, eval(temp_str))


def clear():
    e.delete(0, END)


button0 = Button(root, text="0", padx=40, pady=20, command=lambda : button_click("0"))
button1 = Button(root, text="1", padx=40, pady=20, command=lambda : button_click("1"))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda : button_click("2"))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda : button_click("3"))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda : button_click("4"))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda : button_click("5"))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda : button_click("6"))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda : button_click("7"))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda : button_click("8"))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda : button_click("9"))
buttonDot = Button(root, text=".", padx=40, pady=20, command=lambda : button_click("."))
buttonEqual = Button(root, text="=", padx=40, pady=20, command=ans)
buttonAdd = Button(root, text="+", padx=40, pady=20, command=lambda : button_click("+"))
buttonSub = Button(root, text="-", padx=40, pady=20, command=lambda : button_click("-"))
buttonMul = Button(root, text="*", padx=40, pady=20, command=lambda : button_click("*"))
buttonDiv = Button(root, text="/", padx=40, pady=20, command=lambda : button_click("/"))
buttonClear = Button(root, text="Delete!", padx=80, pady=20,fg="red", command=clear)

button0.grid(row=4, column=1)
buttonDot.grid(row=4, column=0)
buttonEqual.grid(row=4, column=2)
buttonAdd.grid(row=4, column=3)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
buttonSub.grid(row=3, column=3)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
buttonMul.grid(row=2, column=3)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
buttonDiv.grid(row=1, column=3)

buttonClear.grid(row=5, column=0, columnspan=4)

root.mainloop()
