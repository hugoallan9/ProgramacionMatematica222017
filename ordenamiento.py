 #-*-coding:utf-8 -*-
import random
import time
 #Selection sort algorithm

def selectionSort(lista):
    n = len(lista)
    #Variable temporal para guardar el indice del menor 
    min_idx =0
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if lista[min_idx] > lista[j]:
                 min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

numeros = random.sample(range(1000000),10)

#implementacion de insertion sort
def insertionSort(lista):
    n = len(lista)
    for i in range(1,n):
        key = lista[i]
        j = i-1
        while j >=0 and key < lista[j]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = key 
    return lista

inicio = time.time()
numerosOrdenados = insertionSort(numeros)
print time.time() - inicio
print numerosOrdenados
