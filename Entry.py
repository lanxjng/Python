def login():
    email_login = "ukb@gmail.com"
    pass_login = "123456@"
    email_type = entry_email.get()
    pass_type = entry_paw.get()

    if email_login == email_type and pass_login == pass_type:
        showinfo(title="Login", message="Welcome to program <3")
    elif len(email_type) == 0 or len(pass_type) == 0:
        showwarning(title="Warning", message="Moi ban nhap email va password")

    else:
        showwarning(title="Warning", message="Not correct !!")


import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo, showwarning, askyesno

root = tkinter.Tk()
root.title("ENTRY")
root.geometry("400x400")
# root.maxsize(width=800,height=800)
# root.resizable(False,False)
root.config(background="pink")
email = tkinter.StringVar()
password = tkinter.StringVar()
icon_login = tkinter.PhotoImage(file="like.png")
frm = ttk.Frame(root, padding=10)
frm.place(anchor=tkinter.CENTER, relx=0.5, rely=0.5)
lb_email = ttk.Label(frm, text="Email", padding=10)
lb_email.grid(row=0, column=0, sticky=tkinter.W)
entry_email = ttk.Entry(frm, textvariable=email)
entry_email.grid(row=0, column=1, columnspan=2)
lb_paw = ttk.Label(frm, text="Password", padding=10)
lb_paw.grid(row=1, column=0, sticky=tkinter.W)
entry_paw = ttk.Entry(frm, textvariable=password,show="*")
entry_paw.grid(row=1, column=1, columnspan=2)
btn_login = ttk.Button(frm, text="Login", image=icon_login, compound=tkinter.LEFT, command=login)
btn_login.grid(row=2, column=2)

root.mainloop()
