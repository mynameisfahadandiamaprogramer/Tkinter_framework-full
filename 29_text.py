from tkinter import *
root= Tk()

text=Text(root,width=30,height=20,wrap=WORD,padx=10,pady=10,bd=6,selectbackground="green")
text.pack()
root.geometry("400x400")
root.mainloop()