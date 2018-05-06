from tkinter import *

def exitSeq():
    exit()

tk = Tk()


mainFrame = LabelFrame(tk)
mainFrame.pack(side=TOP)

bottomFrame = LabelFrame(tk)
bottomFrame.pack(side=BOTTOM)

centerFrame = LabelFrame(tk)
centerFrame.pack()

label1 = Label(mainFrame, text="press these buttons")
label1.pack()

def but1press():
    label2 = Label(centerFrame, text="buthole")
    label2.pack()
def but2press():
    label3 = Label(centerFrame, text="tits")
    label3.pack()

button1 = Button(mainFrame, text="button1", command=but1press)
button2 = Button(mainFrame, text="button2", command=but2press)
button3 = Button(bottomFrame, text="exit", command=exitSeq)
button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = BOTTOM)


Label(tk, text="First name").grid(row=5)
Label(tk, text="last ").grid(row=6)

ui1 = Entry(tk)
ui2 = Entry(tk)
ui1.grid(row=5,column=1)
ui2.grid(row=6,column=1)

tk.mainloop()