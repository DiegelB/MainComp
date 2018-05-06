from tkinter import *

tk = Tk()

firstFrame = LabelFrame(tk)
firstFrame.grid(row=0, column=0)

def printFunc():
	print("it worked!!!!")


Label(firstFrame, text="hello world!").grid(row=0, column=0)
Button(firstFrame, text="btt1", command=printFunc).grid(row=1, column=2)



tk.mainloop()
