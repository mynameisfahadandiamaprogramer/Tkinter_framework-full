from tkinter import *
root = Tk()

canvs=Canvas(root,width=200,height=200,bg="blue")
canvs.pack()
line=canvs.create_line(0,0,200,100,fill="red")

root.geometry("400x400")
root.mainloop()