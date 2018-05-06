from tkinter import *

global realInput

tk = Tk()

name = StringVar()
Label(tk, text="First name").grid(row=5)
Label(tk, text="last ").grid(row=6)

ui1 = Entry(tk, textvariable=name)

realInput = name.set(ui1.get())

ui2 = Entry(tk)
ui1.grid(row=5,column=1)
ui2.grid(row=6,column=1)


def butt1press():
    Label(tk, text=realInput).grid(row=8,column=2)


Button(tk, text="enter", command=butt1press).grid(row=7,column=1)



tk.mainloop()