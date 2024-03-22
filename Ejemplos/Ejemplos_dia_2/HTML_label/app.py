import tkinter as tk
from tkhtmlview import HTMLText, RenderHTML

root = tk.Tk()
html_label = HTMLText(root, html=RenderHTML('Ejemplos/Ejemplos_dia_2/HTML_label/app.html'))
html_label.pack(fill="both", expand=True)
html_label.fit_height()
root.mainloop()
