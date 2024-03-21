import tkinter as tk

nombre = ""

root = tk.Tk()
root.title("interfaz grafica")

#Label
titulo1 = tk.Label(root,text="Taller Python")
titulo1.grid(row=0,column=1)

labelnombre = tk.Label(root, text="Nombre")
labelnombre.grid(row=1, column=0)

labelapellido = tk.Label(root,text="Apellido")
labelapellido.grid(row=2,column=0)

labeledad = tk.Label(root,text="Edad")
labeledad.grid(row=3,column=0)

#Campo texto
campo_texto_nombre = tk.Entry(root)
campo_texto_nombre.grid(row=1,column=2)

campo_texto_apellido = tk.Entry(root)
campo_texto_apellido.grid(row=2,column=2)

campo_texto_edad = tk.Entry(root)
campo_texto_edad.grid(row=3,column=2)


check_box = tk.Checkbutton(root,text="Acepto")
check_box.grid(row=4,column=1)

def Obtner_entrada():
    nombre = campo_texto_nombre.get()
    apellido = campo_texto_apellido.get()
    edad = campo_texto_edad.get()
    print("Mi nombre es " + nombre +"  "+ apellido + "  Edad es "+ edad)

def Despedida():
    print("!Hasta Pronto!")

def cambiarColor():
    root.config(bg="blue")




#Botones
boton_obtener_entrada = tk.Button(root,text="Obtner entrada", command=Obtner_entrada)
boton_obtener_entrada.grid(row=5, column=0)


boton_obtener_despedida = tk.Button(root,text="Despida",command=Despedida)
boton_obtener_despedida.grid(row=5, column=2)

boton_obtener_color = tk.Button(root,text="Color", command=cambiarColor)
boton_obtener_color.grid(row=5,column=6)

root.mainloop()