def tongChan():
    entry_kq.delete(0, tkinter.END)
    son = int(entry_nhap.get())
    tong_chan = 0
    for i in range(2, son + 1, 2):
        tong_chan += i
    entry_kq.insert(0, f"Tổng là: {tong_chan}")


def tongLe():
    entry_kq.delete(0, tkinter.END)
    son = int(entry_nhap.get())
    tong_le = 0
    for i in range(1, son + 1, 2):
        tong_le += i
    entry_kq.insert(0, f"Tổng là: {tong_le}")


import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.title("Tk")
root.geometry("500x500")
root.maxsize(width=800, height=800)
root.resizable(False, False)
root.config(background="aqua")

n = tkinter.IntVar()

frm = ttk.Frame(root, padding=10)
frm.place(anchor=tkinter.CENTER, relx=0.5, rely=0.5)
lb_nhap = ttk.Label(frm, text="Nhập n", font=("Arial", 30))
lb_nhap.grid(row=0, column=0)
entry_nhap = ttk.Entry(frm, textvariable=n, width=40)
entry_nhap.grid(row=1, column=0)
btn_tongChan = ttk.Button(frm, text="Tính tổng số chẵn", padding=8, command=tongChan)
btn_tongChan.grid(row=2, column=0)
btn_tongLe = ttk.Button(frm, text="Tính tổng số lẻ", padding=8, command=tongLe)
btn_tongLe.grid(row=3, column=0)
entry_kq = ttk.Entry(frm, width=40)
entry_kq.grid(row=4, column=0)

root.mainloop()
