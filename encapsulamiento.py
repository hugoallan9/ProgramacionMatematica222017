

class Persona():
    #Atributo publico
    altura = 1.25
    
    
    
    
    
    
    
    
    def __init__(self, edad,dpi):    
        self.edad = edad
        self.__dpi = dpi
        
    def getDpi(self):
        return self.__dpi
        
    
    
