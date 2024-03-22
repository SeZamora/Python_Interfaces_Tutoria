import tkinter as tk  # Se importa la libreria tkinter


#Se define una funcion para abrir una nueva ventana
def open_new_window():      
    new_window = tk.Toplevel(root) #Se crea la nueva ventana 
    new_window.title("Nueva Ventana")  #Se le da un titulo a la ventana
    new_window.geometry("300x200") #Se define el tamaño de la ventana
    label = tk.Label(new_window, text="Esta es una nueva ventana").pack() #Se agrega una etiqueta a la ventana

root = tk.Tk() #Se declara la interfaz grafica con tkinter
root.title("Ventana Principal") #Se declara el titulo de la ventana principal
root.geometry("400x300") #Se define el tamaño de la ventana

btn_new_window = tk.Button(root, text="Abrir Nueva Ventana", command=open_new_window)#Se crea un boton y se le adjunta la funcion open_new_window
btn_new_window.pack() #se agrega el boton a la ventana principal

root.mainloop() #Se ejecuta la vista principal
