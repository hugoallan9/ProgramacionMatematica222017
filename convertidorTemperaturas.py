# -*- coding:utf-8 -*-
from __future__ import division
# El programa estará diseñado para convertir
# unidades en Fahrenheit a unidades en Celsius
# Programa hecho por: Hugo Garcia

def convertidorFaC(temperaturaF):
    temperaturaC = 5 * ( temperaturaF - 32 ) / 9
    return temperaturaC


print round( convertidorFaC(input( 'Ingresa una temperatura en grados Fahrenheit \n')), 3 ) 
