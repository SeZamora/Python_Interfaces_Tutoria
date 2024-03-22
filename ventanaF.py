from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Ventana Tutoria")

def popup():
    resopnse = messagebox.askyesno("Soy una Ventana Flotante!", "Bienvenido!")
    if resopnse == 1:
        Label(root, text="Diste Yes!").pack()
    else:
        Label(root, text="Diste No!").pack()

Button(root, text="Popup", command=popup).pack()

mainloop()