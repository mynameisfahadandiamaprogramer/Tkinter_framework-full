from tkinter import *
from tkinter.font import Font
root = Tk()

font=Font(size=14,overstrike=1,underline=1)
label=Label(root,text="fahad",font=font)
label.pack()

root.geometry("400x400")
root.mainloop()