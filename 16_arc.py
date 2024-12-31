from tkinter import *
root = Tk()

canvs=Canvas(root,width=200,height=200,bg="blue")
canvs.pack()

canvs.create_arc(100,100,200,200)

root.geometry("400x400")
root.mainloop()