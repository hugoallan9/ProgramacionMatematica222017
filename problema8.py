# -*- coding utf-8 -*-


def leerNumero(ruta):
    archivo = open(ruta, 'r')
    numero =  ''
    for linea in archivo:
        numero  = numero + linea
    return numero

def limpiarCadena(cadena):
    cadenaLimpia = ''
    if cadena.find('\n') == -1:
        cadenaLimpia = cadena
    else:
        posicion = cadena.find('\n')
        cadenaLimpia = cadena[:posicion] + cadena[posicion + 1 : ]
    return cadenaLimpia

def multipicarDigitosCadena(cadena):
    multiplicacion = 1
    listaCadena = list(cadena)
    for x in listaCadena:
        multiplicacion = multiplicacion * int(x)
    return multiplicacion

numero = leerNumero('/mnt/datos/GitHub/ProgramacionMatematica222017/numero.txt')
print multipicarDigitosCadena(limpiarCadena(numero[1:5]))
