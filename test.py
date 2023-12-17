# def notifi():
#     print("Welcome UKB")
def tinh():
    so1_type = int(entry_so1.get())
    so2_type = int(entry_so2.get())
    tong = so1_type + so2_type
    entry_tong.insert(0,f"Tổng là: {tong}")
def luyThua():
    so1_type = int(entry_so1.get())
    so2_type = int(entry_so2.get())
    luythua = so1_type ** so2_type
    entry_lt.insert(0,f"Lũy thừa là: {luythua}")

import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tkinter.Tk()
root.title("Lan Xingtu")
root.geometry("500x500")
root.maxsize(width=800, height=800)
root.resizable(False, False)
root.config(background="pink")
# lb = ttk.Label(root, text="Python", font=("Arial", 20),
#                   background="red", foreground="white", padding=10)
# lb.place(anchor=tkinter.CENTER, relx=0.5, rely=0.5)
# btn = ttk.Button(root, text="UKB", padding=10, command=notifi)
# btn.place(anchor=tkinter.W, relx=0.5, rely=0.5)
# btn1 = ttk.Button(root, text="Exit", padding=10, command=root.destroy)
# btn1.place(anchor=tkinter.E, relx=0.5, rely=0.5)
so1 = tkinter.IntVar()
so2 = tkinter.IntVar()
icon_login = tkinter.PhotoImage(file="like.png")
frm = ttk.Frame(root, padding=10)
frm.place(anchor=tkinter.CENTER, relx=0.5, rely=0.5)
lb_so1 = ttk.Label(frm, text="Số 1", padding=10)
lb_so1.grid(row=0, column=0, sticky=tkinter.W)
entry_so1 = ttk.Entry(frm, textvariable=so1)
entry_so1.grid(row=0, column=1, columnspan=2)
lb_so2 = ttk.Label(frm, text="Số 2", padding=10)
lb_so2.grid(row=1, column=0, sticky=tkinter.W)
entry_so2 = ttk.Entry(frm, textvariable=so2)
entry_so2.grid(row=1, column=1, columnspan=2)
btn_tinh = ttk.Button(frm, text="Phép +", compound=tkinter.LEFT,command=tinh)
btn_tinh.grid(row=2, column=0,pady=15)
entry_tong = ttk.Entry(frm)
entry_tong.grid(row=2, column=2, columnspan=2)
btn_luythua = ttk.Button(frm, text="Lũy Thừa", compound=tkinter.LEFT,command=luyThua)
btn_luythua.grid(row=3, column=0,pady=15)
entry_lt = ttk.Entry(frm)
entry_lt.grid(row=3, column=2, columnspan=2)

root.mainloop()
