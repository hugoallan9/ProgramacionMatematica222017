#-*-coding:utf-8 -*-




def merge(lista,l,m,r):
    n1 = m - l + 1
    n2 = r - m

    # Creando lista izquierda y derecha
    L = [0] * n1
    R = [0] * n2

    #Vaciando la lista en parte izquierda y 
    #derecha

    for a in range(0,n1):
        L[a] = lista[a]
    for b in range(0,n2):
        R[b] = lista[b+m+1]

    #Indices para el merge
    i = 0
    j = 0
    k = 0

    #Haciendo el merge
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            lista[k] = L[i]
            i += 1
        else:
            lista[k] = R[j]
            j += 1
        k += 1
    
    while i < n1:
        lista[k] = L[i]
        i += 1
        k +=1

    while j < n2:
        lista[k] = R[j]
        j += 1
        k += 1

def mergeSort(lista,l,r):
    if l < r:
        m = (l + (r-1) ) / 2
        mergeSort(lista,l,m)
        mergeSort(lista,m+1,r)
    merge(lista,l,m,r)
