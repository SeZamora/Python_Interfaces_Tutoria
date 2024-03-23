import tkinter as tk
from tkinter import ttk

# Importar la librería 'ttk' para crear widgets con un estilo mejorado

# Función que se ejecuta cuando cambia el valor del slider
def slider_changed(event):
    value = slider.get()
    label.config(text=f"Valor seleccionado: {round(value,0)}")

# Crear la ventana principal
root = tk.Tk()
root.title("Slider")  # Establecer el título de la ventana

# Crear una etiqueta para mostrar el valor seleccionado por el slider
label = tk.Label(root, text="Valor seleccionado: ")
label.pack(pady=10)  # Colocar la etiqueta en la ventana

# Crear un slider horizontal con valores de 0 a 100
slider = ttk.Scale(root, from_=0, to=100, orient="horizontal", command=slider_changed)
slider.pack(padx=20, pady=5, fill="x")  # Colocar el slider en la ventana

root.mainloop()  # Ejecutar el bucle principal de la interfaz gráfica
