from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Frames Tutoria")

frame = LabelFrame(root, padx=50, pady=50)
frame.pack(padx=10, pady=10)

frame2 = LabelFrame(root, padx=50, pady=50)
frame2.pack(padx=10, pady=10)

b= Button(frame, text="Boton_Frame1")
b2 = Button(frame, text="Boton_Frame2")


b.grid(row=0, column=0)
b2.grid(row=0, column=1)

root.mainloop()