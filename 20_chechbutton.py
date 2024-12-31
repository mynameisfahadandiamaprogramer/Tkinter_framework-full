from tkinter import *
root = Tk()

def click_me():
    print(i.get())  # Get the current value of the Checkbutton variable

i = IntVar()  # Use IntVar (note the capital "I") to store the state of the Checkbutton
c = Checkbutton(root, text="item1", variable=i)
c.pack()

butn = Button(root, text="click", command=click_me)
butn.pack()

root.geometry("400x400")
root.mainloop()
