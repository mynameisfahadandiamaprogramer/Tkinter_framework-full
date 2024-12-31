from tkinter import *
root = Tk()

def do_nothing():
    print("its a function")

main_menu=Menu(root)
root.config(menu=main_menu)

fileMEnu=Menu(main_menu)
main_menu.add_cascade(label="file",menu=fileMEnu)

#EDIT MENU
edit_menu=Menu(main_menu)
main_menu.add_cascade(label="edit",menu=edit_menu)


fileMEnu.add_command(label="new_project",command=do_nothing)
fileMEnu.add_command(label="new_thing",command=do_nothing)
fileMEnu.add_separator()
fileMEnu.add_command(label="new_xyz",command=do_nothing)
fileMEnu.add_command(label="new_normal function",command=do_nothing)


root.geometry("400x400")
root.mainloop()