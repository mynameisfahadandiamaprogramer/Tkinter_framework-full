from tkinter import *
root = Tk()

frame=Frame(root)
butn=Button(frame,text="button 1")
buton2=Button(frame,text="button 2")

butomFrame=(root)
butn3=Button(butomFrame,text="bottom button")
butn3.pack(side=BOTTOM)
buton2.pack(side=RIGHT)
butn.pack(side=RIGHT)


frame.pack()

root.geometry("400x400")
root.mainloop()