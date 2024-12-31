from tkinter import *
from tkinter import filedialog
root = Tk()

def save_file():
    f=filedialog.asksaveasfile(mode=W,defaultextension=".txt")
    if f is None:
        return
    f.write("hello how are you!!!!!!!")
    f.close()
    
    
        

button=Button(root,text="save_as",command=save_file)
button.pack()
root.geometry("400x400")
root.mainloop()