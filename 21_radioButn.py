from tkinter import *

root = Tk()

def click_me():
    if i.get() == 1:
        print("You are male")
    else:
        print("You are female")

i = IntVar()  # Variable to track the selected Radiobutton

# Creating Radiobuttons for male and female options
r1 = Radiobutton(root, text="Male", value=1, variable=i)
r2 = Radiobutton(root, text="Female", value=2, variable=i)
r1.pack()
r2.pack()

# Button to check the selection
butn = Button(root, text="Check", command=click_me)
butn.pack()

root.geometry("400x400")
root.mainloop()
