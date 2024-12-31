from tkinter import *
root = Tk()

label1=Label(root,text="label")
label2=Label(root,text="label")
label1.place(x=20,y=20)
label2.place(x=20,y=50)


root.geometry("400x400")
root.mainloop()