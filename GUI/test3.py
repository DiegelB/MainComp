from tkinter import *

root = Tk()



label1 = Label( root, text="Noun")
E1 = Entry(root, bd =5)

label2 = Label( root, text="Verb")
E2 = Entry(root, bd =5)

label3 = Label( root, text="Adj.")
E3 = Entry(root, bd =5)

def getDate():
    story = "There once was a little " + E1.get() + " named Jerry." + "He " + E2.get() + " to the market." + "to eat " + E3.get() + " banans."
    label4 = Label(root, text=story)
    label4.grid(row=3, column=1)

submit = Button(root, text ="Submit", command = getDate)

label1.grid(row=0,column=0)
E1.grid(row=0, column=1)
label2.grid(row=1,column=0)
E2.grid(row=1,column=1)
label3.grid(row=2,column=0)
E3.grid(row=2, column=1)
submit.grid(row=2, column=2) 
root.mainloop()
