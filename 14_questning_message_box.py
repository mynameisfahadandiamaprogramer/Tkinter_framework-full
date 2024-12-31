from tkinter import *
from tkinter import messagebox


root = Tk()
def call_me():
    a=messagebox.askquestion("exit","do you want to exit")
    if a == "yes":
        root.quit()

    


butn=Button(root,text="click_me",command=call_me)
butn.pack()


root.geometry("400x400")
root.mainloop()
