#-*- coding:utf-8 -*-
import os
import subprocess



class Escritor():

    def crearFichero(self,ruta):
        fichero = open(ruta, 'w')
        return fichero

    def escribirLinea(self,fichero,linea):
        fichero.write(linea)
        fichero.write("\n")

    def cerrarFichero(self, fichero):
        fichero.close()

    def crearCabecerLatex(self, fichero):
        self.escribirLinea(fichero,'\\documentclass[11pt,twoside]{book}')
        self.escribirLinea(fichero,'\\begin{document}')

    def cerrarDocumentoLatex(self, fichero):
        self.escribirLinea(fichero,'\\end{document}')

    def compilarLatex(self, fichero):
        cadenaCompilacion = "cd " +  os.path.dirname( os.path.realpath(__file__) )+ " & pdflatex  documento.tex & okular documento.pdf"
        print cadenaCompilacion
        subprocess.Popen(cadenaCompilacion, shell=True, stdout =subprocess.PIPE).stdout.read()

escritor = Escritor()
archivo = escritor.crearFichero('/mnt/datos/GitHub/ProgramacionMatematica222017/documento.tex')
#escritor.escribirLinea(archivo, '<!DOCTYPE html>')
#escritor.escribirLinea(archivo, '<html>')
escritor.crearCabecerLatex(archivo)
escritor.escribirLinea(archivo, "Hola Mundo Cruel \\\\")
escritor.escribirLinea(archivo, "$$ ax^2 + bx + c $$ \\\\")
escritor.cerrarDocumentoLatex(archivo)
escritor.cerrarFichero(archivo)
escritor.compilarLatex(archivo)
