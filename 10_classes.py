from tkinter import *

# Function to print the message
def printmessage():
    print("Button clicked!")

# Class definition
class MYbutns:
    def __init__(self, master):
        self.printButton = Button(master, text="Print message", command=printmessage)
        self.printButton.pack(side=LEFT)

# Main application
root = Tk()
b = MYbutns(root)
root.geometry("400x400")
root.mainloop()
