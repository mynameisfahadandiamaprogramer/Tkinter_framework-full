from tkinter import *
from tkinter.scrolledtext import ScrolledText

root = Tk()

sc=ScrolledText(root,width=20,height=10)
sc.pack()
root.geometry("400x400")
root.mainloop()