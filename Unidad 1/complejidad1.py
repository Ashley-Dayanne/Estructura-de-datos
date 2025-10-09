# Análisis teórico de algoritmos (lineal)

import time

def buscar_elemento(lista, elemento):
    for i in range (len(lista)):
        if lista[i] == elemento:
            return True
        return False

starTime = time.time()
en_lista = (1, 2, 3, 4, 5)
elemento = 2
encontrada = buscar_elemento(en_lista, elemento)
endTime = time.time()

if encontrada:
    print("El elemento", elemento, "fue encontrado en la lista")
else:
    print("El elemento", elemento, "no fue encontrado en la lista")
    
