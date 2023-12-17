import tkinter as tk

def calculate_F():
    entry_kq.delete(0, tkinter.END)
    x= int(entry_x.get())
    y= int(entry_y.get())
    if x >= 5:
        F_x = x**3 + (4*x)**2 + 1
    elif x >= 0 and x < 5:
        F_x = x**2 + x + 1
    else:
        F_x = (-2*x)**2 + 5*x + 2

    if y >= 3:
        F_y = (3*x)**2 + 7
    else:
        F_y = 2*x + 4

    result = F_x + F_y
    entry_kq.insert(0, f" {result}")

import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.title("F(x,y)")
root.geometry("500x500")
root.maxsize(width=800, height=800)
root.resizable(False, False)
root.config(background="aqua")

fx = tkinter.IntVar()
fy = tkinter.IntVar()

frm = ttk.Frame(root, padding=10)
frm.place(anchor=tkinter.CENTER, relx=0.5, rely=0.5)
lb_x = ttk.Label(frm, text="Fx", font=("Arial", 30))
lb_x.grid(row=0, column=0)
entry_x = ttk.Entry(frm, textvariable=fx, width=40)
entry_x.grid(row=1, column=0)
lb_y = ttk.Label(frm, text="Fy", font=("Arial", 30))
lb_y.grid(row=2, column=0)
entry_y = ttk.Entry(frm, textvariable=fy, width=40)
entry_y.grid(row=3, column=0)
btn_tinh = ttk.Button(frm, text="F(x,y)", padding=8, command=calculate_F)
btn_tinh.grid(row=4, column=0)
entry_kq = ttk.Entry(frm, width=40)
entry_kq.grid(row=5, column=0)

root.mainloop()