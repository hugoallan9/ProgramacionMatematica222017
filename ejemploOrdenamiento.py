#-*-coding:utf-8 -*-
import random
import time
#Generacion aleatoria de numeros
tiempoInicio = time.time()
numeros =  random.sample(xrange(100000000),10000000)
numeros.sort()
tiempoFin = time.time()
#print numeros
print tiempoFin - tiempoInicio
