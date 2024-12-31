from tkinter import *
from tkinter import messagebox
root = Tk()

def call_me(event=""):
        messagebox.showinfo("trying","this is something important")


root.bind("<Control-c>",call_me)
button=Button(root,text="call_me",command=call_me)
button.pack()

root.geometry("400x400")
root.mainloop()