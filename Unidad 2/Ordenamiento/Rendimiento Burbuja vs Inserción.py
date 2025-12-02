import time
import random

# Función para medir tiempos de ejecución
def medir_tiempo(func, *args):
    inicio = time.time()
    resultado = func(*args)
    final = time.time()
    return resultado, final - inicio

# Ordenamiento burbuja
def burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                # intercambiar los elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Ordenamiento por inserción
def insertion_sort(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista

# Tamaños de prueba
sizes = [100, 1000, 10000]

# Comparación de tiempos
for size in sizes:
    valores = [random.randint(10, 100000) for _ in range(size)]

    # Copias de la misma lista para no alterar los datos originales
    lista_burbuja = valores.copy()
    lista_insercion = valores.copy()

    # Medir tiempos
    _, tiempo_burbuja = medir_tiempo(burbuja, lista_burbuja)
    _, tiempo_insercion = medir_tiempo(insertion_sort, lista_insercion)

    # Mostrar resultados
    print(f"\nTamaño de lista: {size}\n - Burbuja: {tiempo_burbuja:.6f} segundos\n- Inserción: {tiempo_insercion:.6f} segundos")

