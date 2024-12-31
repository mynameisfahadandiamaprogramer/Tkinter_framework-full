from tkinter import *
root = Tk()
def show():
    top=Toplevel()
    top.title("top_window")
    top.geometry("400x400")
    button1=Button(top,text="clik",command=top.destroy)
    button1.pack()


button=Button(root,text="open_window",command=show)
button.pack()
root.geometry("400x400")
root.mainloop()