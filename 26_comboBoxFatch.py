from tkinter import *
from tkinter.ttk import *
def print_me():
    value=combo.get()
    print(value)
root = Tk()
v=["a","b","c","d","e","f"]
combo=Combobox(root,values=v,height=3)
combo.set("select")
combo.pack()

button=Button(root,text="print",command=print_me).pack()
root.geometry("400x400")
root.mainloop()