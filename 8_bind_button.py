from tkinter import *
root = Tk()

def show(event):
    print("I am bind")

button=Button(root, text="click_me")
button.bind("<Button-1>", show)  # Corrected to "<Button-1>"
button.pack()

root.geometry("400x400")
root.mainloop()
