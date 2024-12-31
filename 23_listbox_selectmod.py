from tkinter import *
root = Tk()
l=Listbox(root,width=30,height=15,selectmode=MULTIPLE)#BROWSE,SINGLE,EXTENTED
l.insert(1,"c++")
l.insert(2,"python")
l.insert(3,"java")
l.insert(4,"c#")
l.insert(5,"ruby")
l.insert(6,"js")
l.insert(7,"html")
l.pack()


root.geometry("400x400")
root.mainloop()