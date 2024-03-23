from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Image Viewer Tutoria")

my_img1 = ImageTk.PhotoImage(Image.open("Img/im1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("Img/im2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("Img/im3.png"))

image_list = [my_img1, my_img2, my_img3]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_numbrer):
    global my_label
    global button_forward
    global button_back

    
    my_label.grid_forget()
    my_label = Label(image=image_list[image_numbrer-1])
    if image_numbrer == 3:
        button_forward = Button(root, text=">>", state=DISABLED)
    button_forward = Button(root, text=">>", command=lambda: forward(image_numbrer+1))
    button_back = Button(root, text="<<", command=lambda: back(image_numbrer-1))

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

def back(image_numbrer):
    global my_label
    global button_forward
    global button_back



    
    my_label.grid_forget()
    my_label = Label(image=image_list[image_numbrer-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_numbrer+1))
    button_back = Button(root, text="<<", command=lambda: back(image_numbrer-1))

    if image_numbrer == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

button_back = Button(root, text="<<", command= back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()