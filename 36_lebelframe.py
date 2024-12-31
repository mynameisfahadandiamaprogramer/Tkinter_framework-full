from tkinter import *
root = Tk()
frame=LabelFrame(root,text="input",padx=5,pady=5)
frame.pack()
entry=Entry(frame)
entry.pack()
root.geometry("400x400")
root.mainloop()