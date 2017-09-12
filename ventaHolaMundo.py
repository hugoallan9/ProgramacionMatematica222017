import Tkinter as tk

class Aplicacion():

    def __init__(self,master):
        frame = tk.Frame(master)
        frame.pack()

        self.boton = tk.Button(
            frame, text="Salir", fg ="red", command = frame.quit
        )


        self.boton.pack(side=tk.LEFT)
        self.botonSaludar = tk.Button(
            frame, text="Saludar!", fg="blue", command=self.saludar)
        self.botonSaludar.pack(side=tk.LEFT)

    def saludar(self):
        self.Etiqueta = tk.Label(text="Hola Mundo Cruel")
        #self.Etiqueta.pack(side=tk.LEFT)
        print "Hola Mundo Cruel"

root = tk.Tk()
app = Aplicacion(root)
root.mainloop()
