from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Check Tutoria")

TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Jamon", "Jamon"),
    ("Tocino", "Tocino"),
]

pizza = StringVar() 
pizza.set("Pepperoni")

for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

myButton = Button(root, text="Click Me!", command=lambda: clicked(pizza.get()))
myButton.pack()

mainloop()