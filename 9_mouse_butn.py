from tkinter import *
root = Tk()

def rightclick(event):
    print("It's right click")

def leftclick(event):
    print("It's left click")

def middle(event):
    print("Middle button is clicked")

button = Button(root, text="Click me")
button.pack()

# Binding mouse events to the button
button.bind("<Button-1>", leftclick)  # Left click
button.bind("<Button-2>", middle)    # Middle click
button.bind("<Button-3>", rightclick)  # Right click

root.geometry("400x400")
root.mainloop()
