from tkinter import *
root = Tk()

def print_me():
    items=l.curselection()
    print(items)
    for item in items:
        print(l.get(item))

def delete_me():
    clicked_items = l.curselection()
    for item in clicked_items:
        print(l.delete(item))

l=Listbox(root,width=30,height=15,selectmode=MULTIPLE)#BROWSE,SINGLE,EXTENTED
l.insert(1,"c++")
l.insert(2,"python")
l.insert(3,"java")
l.insert(4,"c#")
l.insert(5,"ruby")
l.insert(6,"js")
l.insert(7,"html")
l.pack()
buttob=Button(root,text="select",command=print_me)
buttob.pack()

button_delete=Button(root,text="delete",command=delete_me)
button_delete.pack()

root.geometry("400x400")
root.mainloop()