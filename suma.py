import tkinter as tk

def sumar_numero():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado.set(num1 +num2)

root = tk.Tk()
root.title("Suma Numeros")

entrada1 = tk.Entry(root)
entrada1.grid(row=0,column=0)

entrada2 = tk.Entry(root)
entrada2.grid(row=0,column=1)

etiqueta_mas = tk.Label(root, text="+")
etiqueta_mas.grid(row=0, column=2)

# Etiqueta de resultado con StringVar para actualizaciones dinámicas
resultado = tk.StringVar()
etiqueta_resultado = tk.Label(root, textvariable=resultado)
etiqueta_resultado.grid(row=1, column=2)


boton_suma = tk.Button(root,text="Sumar", command=sumar_numero)
boton_suma.grid(row=2, column=1)

root.mainloop()