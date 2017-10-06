try:
    import cPickle as pickle
except ImportError:
    import pickle


class Jugador():
    
    def __init__(self,nombre):
        self.nombre = nombre
        
        
        
        
        
    def asignarPunteo(self,punteo):
        self.punteo = punteo
        
    def asignarTiempo(self,tiempo):
        self.tiempo = tiempo
        
    
 
 
def guardarPartida(archivoSalida,datos):
    archivo = open(archivoSalida, 'w')
    for nombre, puntaje, tiempo in datos:
        archivo.write(nombre + "," + str(puntaje) + "," + tiempo + "\n"   )
    archivo.close()
    
    
 
 
def recuperarPartida(archivoEntrada):
    archivo = open(archivoEntrada, 'r')
    datos = []
    for linea in archivo:
        nombre, puntaje, tiempo = linea.rstrip("\n").split(',')
        datos.append( (nombre, int(puntaje), tiempo  ) )
    archivo.close()
    return datos

#juego = [("Adriana", 120, "1:20"), ("Luis", 11, "0:10"), ("Luz", 100, "1:00")]
#guardarPartida("partidas.txt", juego)

#juegoRecuperado = []
#juegoRecuperado = recuperarPartida("partidas.txt")
#print juegoRecuperado


adriana = Jugador("Adriana")
adriana.asignarPunteo(150)
adriana.asignarTiempo("1:30")

archivo = open("jugadores.mat", "w")
pickle.dump(adriana, archivo,1)
archivo.close()

#Abriendo archivo donde se encuentra guardado el objeto
fichero = open('jugadores.mat', 'r')
adri = pickle.load(fichero)
print adri.nombre
adri.asignarPunteo(190)
print adri.punteo




