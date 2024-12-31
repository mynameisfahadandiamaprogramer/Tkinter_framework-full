from tkinter import *
from tkinter import filedialog

root = Tk()

def open_file():
    # Open file dialog to select multiple files
    result = filedialog.askopenfiles(initialdir="/", title="Select File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    print("Selected Files:")
    for file in result:
        print(f"File: {file.name}")  # Print the file name

        content = file.read()  # Read the file content
        print(content)  # Print the content of the file
        
        file.close()  # Close the file after reading

button = Button(root, text="Open File", command=open_file)
button.pack()
root.geometry("400x400")
root.mainloop()
