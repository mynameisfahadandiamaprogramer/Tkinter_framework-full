from tkinter import *
root = Tk()

def callme():
    print("i am called")

button=Button(root,text="click_me",command=callme)
button.pack()
root.geometry("400x400")
root.mainloop()