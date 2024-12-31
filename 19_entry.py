from tkinter import *
root = Tk()
def click_me():
    print(entry.get())


entry=Entry(root)
entry.pack()

butn=Button(root,text="click",command=click_me)
butn.pack()

root.geometry("400x400")
root.mainloop()