from tkinter import *
root = Tk()
label=Label(root,text="label",bg="red",fg="blue")
label2=Label(root,text="labale 2",bg="black",fg="white")

label.pack(fill=X)
label2.pack(side=LEFT,fill=Y)


root.geometry("400x400")
root.mainloop()