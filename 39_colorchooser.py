from tkinter import *
from tkinter import colorchooser
root = Tk()
def show():
    colr=colorchooser.askcolor(title="select_colcor")
    root.configure(background=colr[1])

button=Button(root,text="change_color",command=show)
button.pack()

root.geometry("400x400")
root.mainloop()