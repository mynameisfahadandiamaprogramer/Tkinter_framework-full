from tkinter import *
root = Tk()

def show():
    print(spin.get())
spin=Spinbox(root,from_=1,to=4)
spin.pack()

button=Button(root,text="click",command=show)
button.pack()

root.geometry("400x400")
root.mainloop()