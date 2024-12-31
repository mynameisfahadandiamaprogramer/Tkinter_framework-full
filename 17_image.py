from tkinter import *
from PIL import Image, ImageTk  # Pillow library is required

# Create the main window
root = Tk()
root.title("Simple Tkinter Image Example")

# Load an image file (replace "example.png" with your image file)
image_path = "circle.ico"  # Replace with the path to your image
image = Image.open(image_path)
image = image.resize((200, 200))  # Resize the image
photo = ImageTk.PhotoImage(image)

# Add the image to the window
label_image = Label(root, image=photo)
label_image.pack(pady=20)


# Run the application
root.mainloop()
