# Algoritmo de Búsqueda Binaria

def busqueda_binaria(lista, objetivo):
    low, high = 0, len(lista) - 1
    while low <= high:
        mid = (low + high) // 2
        if lista[mid] == objetivo:
            return mid
        elif lista[mid] < objetivo:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Ejemplo de uso
datos = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
valor_buscado = 23

resultado = busqueda_binaria(datos, valor_buscado)

if resultado != -1:
    print(f"El valor {valor_buscado} se encuentra en la posición {resultado}.")
else:
    print(f"El valor {valor_buscado} no se encuentra en la lista.")
