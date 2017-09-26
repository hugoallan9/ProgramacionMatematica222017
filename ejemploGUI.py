#from tkinter import *

import tkinter as tk

ventana = tk.Tk()







def getDimensions():
    ventana.update()
    print ('El ancho de la ventana es: ', ventana.winfo_width() )
    print ('El alto de la ventan es: ', ventana.winfo_height() )
    

def increaseSize():
    ventana.minsize(1024,ventana.winfo_height()) 

getDimensions()
increaseSize()
getDimensions()

ventana.mainloop()
