def confirm():
    answer = askyesno(title="Confirmation", message="Are you sure ??")
    if answer:
        root.destroy()


import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo, showwarning, askyesno
from functools import partial

# root = tkinter.Tk()
# root.title("Tkinter GUI Example")
# root.geometry("400x300")
# frm = ttk.Frame(root, padding =10)
# frm.place(anchor = tkinter.CENTER, relx= 0.5, rely=0.5)
# label_hello = ttk.Label(frm,text="Hello World",font=('Arial',24),foreground='red')
# label_hello.grid(row=0, column=0)
# btn_exit=ttk.Button(frm,text="Quit",command= root.destroy)
# btn_exit.grid(row=1,column=0)
root = tkinter.Tk()
root.title("Button")
root.geometry("500x500")
root.maxsize(width=800, height=800)
root.resizable(False, False)
root.config(background="pink")
frm = ttk.Frame(root, padding=10)
icon_like = tkinter.PhotoImage(file="like.png")
icon_unlike = tkinter.PhotoImage(file="dislike.png")
icon_quit = tkinter.PhotoImage(file="close.png")
frm.place(anchor=tkinter.CENTER, relx=0.5, rely=0.5)
btn_like = ttk.Button(frm, text="Like", padding=8, image=icon_like, compound=tkinter.LEFT,
                      command=partial(
                          showinfo,
                          title="Information",
                          message="Button Like Clicked"
                      ))
btn_like.grid(row=0, column=0)
btn_unlike = ttk.Button(frm, text="UnLike", padding=8, image=icon_unlike, compound=tkinter.LEFT,
                        command=partial(
                            showwarning,
                            title="Warning",
                            message="Button Dislike Cliked"
                        ))
btn_unlike.grid(row=1, column=0)
btn_quit = ttk.Button(frm, text="Quit", padding=8, image=icon_quit, compound=tkinter.LEFT,
                      command=confirm)
btn_quit.grid(row=2, column=0)
btn_check = ttk.Button(frm, text="Check", padding=8, state="disable")
btn_check.grid(row=3, column=0)
root.mainloop()
