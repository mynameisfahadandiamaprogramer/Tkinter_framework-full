from tkinter import *
from tkinter import messagebox


root = Tk()
def call_me():
    messagebox.showinfo("success","installation complete")
butn=Button(root,text="click_me",command=call_me)
butn.pack()


root.geometry("400x400")
root.mainloop()
