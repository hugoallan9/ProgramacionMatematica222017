import tkinter as tk
from tkinter import Menu
from tkinter import ttk
from ixion import column_label

ventana = tk.Tk()

ventana.title("El pack de Mack")




barraMenu = Menu()

ventana.config(menu=barraMenu)

fileMenu = Menu(barraMenu, tearoff=0)
fileMenu.add_command(label="Nuevo")
fileMenu.add_separator()
fileMenu.add_command(label="Editar")
fileMenu.add_separator()

ventana.config(menu=fileMenu)


texto = tk.StringVar()

opciones = ttk.Combobox(ventana, width=12,textvariable = texto)
opciones['values'] = ("Pizza", "Hamburguesa","Papas") 
opciones.grid(column=1, row=0)
opciones.current(0)





ventana.mainloop()