from tkinter import *
root = Tk()

name = Label(root, text="name")
password = Label(root, text="password")
entry = Entry(root)
entry2 = Entry(root)  # This will mask the password input
checkButn=Checkbutton(root,text="keep me logIn")

name.grid(row=0, column=0,sticky=E)
entry.grid(row=0, column=1)
password.grid(row=1, column=0)
entry2.grid(row=1, column=1)  # Change column to 1

checkButn.grid(columnspan=2)

root.geometry("400x400")
root.mainloop()
