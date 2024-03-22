import tkinter as tk

root = tk.Tk()
root.title("Ejemplo 1")


label1 = tk.Label(root,text="Taller Python")

label1.grid(row=0,column=1)

def mynombre():
    print("Mi nombre")




campo_texto = tk.Entry(root)
campo_texto.grid(row=4, column=1)


def obtener_entrada():
    entrada = campo_texto.get()
    print("El usuario ingresado ", entrada)

button = tk.Button(root, text="Mensaje", command=obtener_entrada)
button.grid(row=3,column=5)





root.mainloop()