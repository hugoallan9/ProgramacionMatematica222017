#-*-coding:utf-8 -*-

import random
import time

def ordenamientoBurbuja(lista):
    temporal = 0
    n = len(lista)
    for i in range(n):
        for j in range(n):
            if lista[i] < lista[j]:
                temporal = lista[j]
                lista[j] = lista[i]
                lista[i] = temporal
    return lista

def ordenamientoBurbuja1(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

def ordenamientoBurbujaMejorado(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0,n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


numero = random.sample(range(10000000), 10000)
#print numero
t10 = time.time()
ordenamientoBurbuja(numero)
t11 = time.time()
print t11 - t10
t20 = time.time()
ordenamientoBurbuja1(numero)
t21 = time.time()
print t21 - t20
t30 = time.time()
ordenamientoBurbujaMejorado(numero)
t31 = time.time()
print t31 - t30