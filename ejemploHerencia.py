# -*- coding: utf-8 -*-

class Persona():
    cui = 0
    estadoCivil = 'Soltero'

    def __init__(self, cui, estadoCivil):
        self.cui = cui
        self.estadoCivil = estadoCivil
        self.nacer(cui)


    def nacer(self, cui):
        self.cui = cui


class Registrador(Persona):
    numeroEmpleado = 0
    puesto = "normal"
    fechaAlta = 0

    def __init__(self, cui, noEmpleado, position, fechaAlta):
        #super(self.__class__, self).__init__(cui," Soltero ")
        self.cui = cui
        self.numeroEmpleado = noEmpleado
        self.puesto = position
        self.fechaAlta = fechaAlta

    def registar(self, cui):
        personaNueva = Persona(cui, "Soltero")
        return personaNueva

registrador1 = Registrador("2521 01156 0101",1,"Jefe", "12-08-2017")
personaRegistrada = registrador1.registar("2530 05151 0101")
print personaRegistrada.cui
print personaRegistrada.estadoCivil
print registrador1.cui
print registrador1.numeroEmpleado
#registrador1.cui = "2521 01156 0101"
print registrador1.cui
