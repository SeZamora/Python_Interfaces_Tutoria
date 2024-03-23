import tkinter as tk
from tkinter import filedialog

# Función para abrir el cuadro de diálogo de archivos y mostrar el archivo seleccionado en un Label
def open_file_dialog():
    file_path = filedialog.askopenfilename()  # Obtener la ruta del archivo seleccionado
    try:
        # Leer el contenido del archivo
        with open(file_path, 'r') as file:
            content = file.read()
        # Dividir el contenido en líneas de máximo 50 caracteres
        lines = [content[i:i+52] for i in range(0, len(content), 50)]
        # Unir las líneas con saltos de línea
        content_formatted = '\n'.join(lines)
        # Actualizar el contenido del Label
        label.config(text=f"Contenido del archivo:\n{content_formatted}")
    except Exception as e:
        # Manejar cualquier error al leer el archivo
        label.config(text=f"Error al abrir el archivo:\n{str(e)}")

# Crear la ventana principal
root = tk.Tk()
root.title("Cuadro de Diálogo de Archivos")  # Establecer el título de la ventana

# Crear un botón para abrir el cuadro de diálogo de archivos
btn_open_dialog = tk.Button(root, text="Abrir Archivo", command=open_file_dialog)
btn_open_dialog.pack()  # Colocar el botón en la ventana

# Crear un Label para mostrar el contenido del archivo seleccionado
label = tk.Label(root, text="Contenido del archivo:")
label.pack(pady=10)  # Colocar el Label en la ventana con un poco de espacio

root.mainloop()  # Ejecutar el bucle principal de la interfaz gráfica
