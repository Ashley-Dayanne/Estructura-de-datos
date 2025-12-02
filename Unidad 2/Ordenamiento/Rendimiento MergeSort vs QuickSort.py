import time
import random

# Función para medir tiempos de ejecución
def medir_tiempo(func, *args):
    inicio = time.time()
    resultado = func(*args)
    final = time.time()
    return resultado, final - inicio

# -------------------- MERGE SORT --------------------
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]
    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)
    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# -------------------- QUICK SORT --------------------
def particion(lista, inicio, fin):
    pivote = lista[fin]
    i = inicio - 1
    for j in range(inicio, fin):
        if lista[j] <= pivote:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[fin] = lista[fin], lista[i + 1]
    return i + 1

def quicksort(A, inicio, fin):
    if inicio < fin:
        indice_pivote = particion(A, inicio, fin)
        quicksort(A, inicio, indice_pivote - 1)
        quicksort(A, indice_pivote + 1, fin)

# -------------------- PRUEBA Y COMPARACIÓN --------------------
sizes = [100, 1000, 10000]

for size in sizes:
    valores = [random.randint(10, 100000) for _ in range(size)]

    lista_merge = valores.copy()
    lista_quick = valores.copy()

    # Medir tiempos
    _, tiempo_merge = medir_tiempo(mergeSort, lista_merge)
    _, tiempo_quick = medir_tiempo(quicksort, lista_quick, 0, len(lista_quick) - 1)

    # Mostrar resultados
    print(f"\nTamaño de lista: {size}")
    print(f"- Merge Sort: {tiempo_merge:.6f} segundos")
    print(f"- Quick Sort: {tiempo_quick:.6f} segundos")

