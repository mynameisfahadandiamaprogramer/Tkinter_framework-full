from tkinter import *

# Create the main window
root = Tk()

# Create a frame to hold the listbox and scrollbar
frame = Frame(root)
frame.pack(side=LEFT)

# Create the scrollbar
scrol = Scrollbar(frame)
scrol.pack(side=RIGHT, fill=Y)

# Create the listbox and link it to the scrollbar
listbox = Listbox(frame, yscrollcommand=scrol.set)
for i in range(1, 100):
    listbox.insert(END, "list" + str(i))
listbox.pack()

# Configure the scrollbar to work with the listbox
scrol.config(command=listbox.yview)

# Set the size of the main window
root.geometry("400x400")

# Start the main event loop
root.mainloop()
