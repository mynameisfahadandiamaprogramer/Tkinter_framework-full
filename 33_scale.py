from tkinter import *
root = Tk()
s=Scale(root,from_=0,to=100,orient=HORIZONTAL,length=200,width=10,sliderlength=50)
s.set(100)
print(s.get())
s.pack(side=LEFT)

root.geometry("400x400")
root.mainloop()