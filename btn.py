# def up():
#     size = myFont["size"]
#     myFont.configure(size=size + 2)
#
#
# def down():
#     size = myFont["size"]
#     myFont.configure(size=size - 2)
# def submit():
#     data = text_cmt.get(1.0, 5.0).strip()
#     if len(data) == 0:
#         showwarning(title="Warning", message="Empty")
#     else:
#         showinfo(title="Your comment", message=data)
def drink_change():
    if coca.get() == 1:
        drink.add("Coca")
    elif "Coca" in drink:
        drink.remove("Coca")
    if pepsi.get() == 1:
        drink.add("Pepsi")
    elif "Pepsi" in drink:
        drink.remove("Pepsi")
    if milk.get() == 1:
        drink.add("Milk")
    elif "Milk" in drink:
        drink.remove("Milk")
    if orange.get() == 1:
        drink.add("Orange")
    elif "Orange" in drink:
        drink.remove("Orange")
    if yomost.get() == 1:
        drink.add("Yomost")
    elif "Yomost" in drink:
        drink.remove("Yomost")


def submit():
    my_drink = ""
    for i in drink:
        my_drink += i + "\n"
    showinfo(title="Your drink", message=my_drink)


import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo, showwarning
from tkinter import font

root = tkinter.Tk()
root.title("ORDER DRINK")
root.geometry("400x400")
root.maxsize(width=800, height=800)
root.resizable(False, False)
root.config(background="pink")
# myFont = font.Font(family="Arial", size=15)
frm = ttk.Frame(root, padding=10)
frm.place(anchor=tkinter.CENTER, relx=0.5, rely=0.5)
# lb = ttk.Label(frm, text="Python", font=myFont,
#                   background="red", foreground="white", padding=10)
# lb.grid(row=0, column=0)
# btn_up = ttk.Button(frm, text="+", padding=10, command=up)
# btn_up.grid(row=1, column=0)
# btn_down = ttk.Button(frm, text="-", padding=10, command=down)
# btn_down.grid(row=2, column=0)
# text_cmt = tkinter.Text(frm, height=15, width=40)
# text_cmt.grid(row=0, column=0)
# btn_sub = ttk.Button(frm, text="Submit", padding=10, command=submit)
# btn_sub.grid(row=1, column=0, pady=10)
coca = tkinter.IntVar()
pepsi = tkinter.IntVar()
milk = tkinter.IntVar()
orange = tkinter.IntVar()
yomost = tkinter.IntVar()

drink = set()
# v=tkinter.IntVar()
# rd1 = ttk.Radiobutton(frm,text="Nam",variable=v,value=1)
# rd1.grid(row=1, column=0, sticky=tkinter.W)
# rd2 = ttk.Radiobutton(frm,text="Nam",variable=v,value=2)
# rd2.grid(row=1, column=0, sticky=tkinter.W)

check_coca = ttk.Checkbutton(frm, text="coca", variable=coca, command=drink_change)
check_coca.grid(row=0, column=0, sticky=tkinter.W)
check_pepsi = ttk.Checkbutton(frm, text="pepsi", variable=pepsi, command=drink_change)
check_pepsi.grid(row=1, column=0, sticky=tkinter.W)
check_milk = ttk.Checkbutton(frm, text="milk", variable=milk, command=drink_change)
check_milk.grid(row=2, column=0, sticky=tkinter.W)
check_orange = ttk.Checkbutton(frm, text="orange", variable=orange, command=drink_change)
check_orange.grid(row=3, column=0, sticky=tkinter.W)
check_yomost = ttk.Checkbutton(frm, text="yomost", variable=yomost, command=drink_change)
check_yomost.grid(row=4, column=0, sticky=tkinter.W)
btn_sub = ttk.Button(frm, text="Submit", padding=10, command=submit)
btn_sub.grid(row=5, column=0, pady=10)
root.mainloop()
