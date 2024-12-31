from tkinter import *
root = Tk()
def show():
    top=Toplevel()
    top.title("multipul windows")
    button = Button(top,text="destoy",command=top.destroy)
    button.pack()


button=Button(root,text="click",command=show)
button.pack()
root.geometry("400x400")
root.mainloop()