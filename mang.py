def catChuoi():
    entry_kq.delete(0, tkinter.END)
    arr = entry_nhap.get().split(",")
    array = []
    for x in arr:
        array.append(int(x))
    return array
def tinhTong():
    entry_kq.insert(0, str(sum(catChuoi())))


def timLe():
    array = catChuoi()
    s = ""
    array.sort()
    for i in array:
        if i % 2 != 0:
            s += str(i) + ","
    s = s[0:len(s) - 1]
    entry_kq.insert(0, s)


def timChan():
    array = catChuoi()
    s = ""
    array.sort()
    for i in array:
        if i % 2 == 0:
            s += str(i) + ","
    s = s[0:len(s) - 1]
    entry_kq.insert(0, s)


def maxMin():
    entry_kq.insert(0, "Max: " + str(max(catChuoi())) + " | Min: " + str(min(catChuoi())))


import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.title("Chương trình thao tác với mảng")
root.geometry("500x500")
root.maxsize(width=800, height=800)
root.resizable(False, False)
root.config(background="pink")

arr = tkinter.StringVar()

frm = ttk.Frame(root, padding=10)
frm.place(anchor=tkinter.CENTER, relx=0.5, rely=0.5)
lb_nhap = ttk.Label(frm, text="Nhập mảng", font=("Arial", 30))
lb_nhap.grid(row=0, column=0, sticky=tkinter.W)
entry_nhap = ttk.Entry(frm, textvariable=arr, width=45)
entry_nhap.grid(row=1, column=0, sticky=tkinter.W)
btn_tong = ttk.Button(frm, text="Tính tổng mảng", padding=15, width=40, command=tinhTong)
btn_tong.grid(row=2, column=0, sticky=tkinter.W)
btn_chan = ttk.Button(frm, text="Tìm phần tử chẵn", padding=15, width=40, command=timChan)
btn_chan.grid(row=3, column=0, sticky=tkinter.W)
btn_le = ttk.Button(frm, text="Tìm phần tử lẻ", padding=15, width=40, command=timLe)
btn_le.grid(row=4, column=0, sticky=tkinter.W)
btn_maxmin = ttk.Button(frm, text="Tìm max,min của mảng", padding=15, width=40, command=maxMin)
btn_maxmin.grid(row=5, column=0, sticky=tkinter.W)
lb_kq = ttk.Label(frm, text="Kết quả tính toán", font=("Arial", 30))
lb_kq.grid(row=6, column=0, sticky=tkinter.W)
entry_kq = ttk.Entry(frm, width=45)
entry_kq.grid(row=7, column=0, sticky=tkinter.W)

root.mainloop()
