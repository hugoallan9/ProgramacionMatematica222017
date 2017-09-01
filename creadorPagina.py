#-*- coding:utf-8 -*-

class Escritor():

    def crearFichero(self,ruta):
        fichero = open(ruta, 'w')
        return fichero

    def escribirLinea(self,fichero,linea):
        fichero.write(linea)
        fichero.write("\n")

    def cerrarFichero(self, fichero):
        fichero.close()


escritor = Escritor()
archivo = escritor.crearFichero('/mnt/datos/GitHub/ProgramacionMatematica222017/paginaNueva.html')
escritor.escribirLinea(archivo, '<!DOCTYPE html>')
escritor.escribirLinea(archivo, '<html>')
escritor.cerrarFichero(archivo)
