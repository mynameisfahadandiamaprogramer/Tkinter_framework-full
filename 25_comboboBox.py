from tkinter import *
from tkinter.ttk import *

root = Tk()
v=["a","b","c","d","e","f"]
combo=Combobox(root,values=v,height=3)
combo.set("select")
combo.pack()


root.geometry("400x400")
root.mainloop()