import Tkinter as tk

class Aplicacion():

    def __init__(self,master):
        frame = tk.Frame(master,width=768, height=576, bg="", colormap="new")
        frame.pack()

        self.boton = tk.Button(
            frame, text="Salir", fg ="red", command = frame.quit
        )


        self.boton.pack(side=tk.LEFT)
        self.botonSaludar = tk.Button(
            frame, text="Saludar!", fg="blue", command=self.saludar)
        self.botonSaludar.pack(side=tk.LEFT)
        self.Entrada = tk.Entry(frame)
        self.Entrada.pack()


        self.ButonEntrada = tk.Button(
            frame, text="Listo", fg="blue", command=self.callBack)
        self.ButonEntrada.pack()



    def saludar(self):
        self.Etiqueta = tk.Label(text="Hola Mundo Cruel")
        self.Etiqueta.pack(side=tk.LEFT)
        print "Hola Mundo Cruel"

    def callBack(self):
        self.TextoEntrada = self.Entrada.get()
        self.Entrada.delete(0,len(self.TextoEntrada))
        print self.TextoEntrada

root = tk.Tk()
app = Aplicacion(root)
root.mainloop()
