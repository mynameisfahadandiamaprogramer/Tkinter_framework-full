from tkinter import *
from tkinter import simpledialog
root = Tk()
def get_me():
    s=simpledialog.askstring("input_string","plese enter your name")
    print(s)

button=Button(root,text="pupup",command=get_me)
button.pack()
root.geometry("400x400")
root.mainloop()