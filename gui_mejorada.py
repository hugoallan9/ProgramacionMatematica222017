'''
Created on Septiembre de  2017
@author: Hugo Garcia
'''





#======================
# importaciones
#======================
import tkinter as tk
from tkinter import Menu
from tkinter import ttk
from typing import overload
from _snack import label
        
#======================
# funciones
#======================
# Exit GUI cleanly
def _quit():
    ventana.quit()      
    ventana.destroy()
    exit() 

#======================
# procedural code
#======================
# Create instance
ventana = tk.Tk()   

# Add a title       
ventana.title("Ventana de prueba")
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# Creating a Menu Bar
menuBar = Menu()
ventana.config(menu=menuBar)

# Add menu items
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Nuevo")
fileMenu.add_separator()
fileMenu.add_command(label="Salir", command=_quit)   # command callback
menuBar.add_cascade(label="Archivo", menu=fileMenu)

# Add another Menu to the Menu Bar and an item
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="Acerca de")
menuBar.add_cascade(label="Ayuda", menu=helpMenu)

editMenu = Menu(menuBar, tearoff = 0)
editMenu.add_command(label="Copiar")
editMenu.add_command(label="Pegar")
menuBar.add_cascade(label="Editar", menu = editMenu)
# ---------------------------------------------------------------

# Tab Control / Notebook introduced here ------------------------
tabControl = ttk.Notebook(ventana)          # Create Tab Control

tab1 = ttk.Frame(tabControl)            # Create a tab 
tabControl.add(tab1, text='Pestaña 1')      # Add the tab

tab2 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab2, text='Pestaña 2')      # Make second tab visible

tabControl.pack(expand=1, fill="both")  # Pack to make visible
# ---------------------------------------------------------------

# ---------------------------------------------------------------    
# We are creating a container frame to hold all other widgets
primerframe = ttk.LabelFrame(tab1, text=' Primer Frame ')
# using the tkinter grid layout manager
primerframe.grid(column=0, row=0, padx=28, pady=15)

# ---------------------------------------------------------------
# but frame won't be visible until we add widgets to it...
# Adding a Label
ttk.Label(primerframe, text="Comida para llevar:").grid(column=0, row=0, sticky='E')

#Creating the combobox
# ---------------------------------------------------------------
texto = tk.StringVar()
comidaSeleccionada = ttk.Combobox(primerframe, width=12, textvariable=texto)
comidaSeleccionada['values'] = ('Frutas', 'Hamburguesa', 'Pizza', 'Pasta al pesto')
comidaSeleccionada.grid(column=1, row=0)
comidaSeleccionada.current(0)                 # highlight first city
        
# ---------------------------------------------------------------
# increase combobox width to longest city
max_width  = max([len(x)for x in comidaSeleccionada['values']])
new_width = max_width
# new_width = max_width - 4             # adjust per taste of extra spacing
comidaSeleccionada.config(width=new_width)
    
# ---------------------------------------------------------------   
#==========================
ENTRY_WIDTH = max_width + 3             # adjust per taste of alignment
#==========================
# Adding Label & Textbox Entry widgets
#---------------------------------------------
ttk.Label(primerframe, text="Edad").grid(column=0, row=1, sticky='E')         # <== right-align
updated = tk.StringVar()
updatedEntry = ttk.Entry(primerframe, width=ENTRY_WIDTH, textvariable=updated, state='readonly')
updatedEntry.grid(column=1, row=1, sticky='W')




#======================
# Start GUI
#======================
ventana.mainloop()
