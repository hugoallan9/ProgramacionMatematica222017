# -*- coding utf-8 -*-
import time

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
    if len(listaCadena) == 14:
        listaCadena.pop()

    for x in listaCadena:
        multiplicacion = multiplicacion * int(x)
    return multiplicacion

def resolverProblema():
    inicio = time.time()
    numero = leerNumero('/mnt/datos/GitHub/ProgramacionMatematica222017/numero.txt')
    productoMaximo = 0
    productoTmp = 0
    for x in range(0,987):
        productoTmp = multipicarDigitosCadena( limpiarCadena( numero[x : x + 14] ) )
        if productoTmp > productoMaximo:
            productoMaximo = productoTmp
    fin = time.time()
    print   fin - inicio
    return productoMaximo

numero = leerNumero('/mnt/datos/GitHub/ProgramacionMatematica222017/numero.txt')
#print limpiarCadena( numero[ 45: 45 + 13] )
#print limpiarCadena( numero[ 0: 0 + 13] )
print resolverProblema()
