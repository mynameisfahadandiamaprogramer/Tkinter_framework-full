from tkinter import *

def print_me():
    try:
        result = text.selection_get()
        print(result)
    except:
        print("No text selected")

def delete_selection():
    try:
        text.delete(SEL_FIRST, SEL_LAST)  # Delete selected text
    except:
        print("No text selected to delete")

# Create the main application window
root = Tk()

# Create a Text widget
text = Text(root, width=30, height=20, wrap=WORD, padx=10, pady=10, bd=6, selectbackground="green")
text.pack()

# Insert initial text
text.insert(INSERT, "Hello, I am Fahad")

# Create the "Print" button
button_print = Button(root, text="Print", command=print_me)
button_print.pack()

# Create the "Delete" button
button_delete = Button(root, text="Delete", command=delete_selection)
button_delete.pack()

# Set the window size
root.geometry("400x400")

# Run the Tkinter event loop
root.mainloop()
