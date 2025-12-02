import random

# ------------------ CREACIÓN DE DATOS ------------------
# Generar 100 productos con puntuaciones aleatorias de relevancia
productos = []
for i in range(1, 101):
    producto = {
        "nombre": f"Producto_{i}",
        "puntuacion": random.randint(1, 100)
    }
    productos.append(producto)


# ------------------ MERGE SORT ----------------------
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


# ------------------ APLICACIÓN DEL ORDENAMIENTO ------------------
# Extraer las puntuaciones de los productos
puntuaciones = [p["puntuacion"] for p in productos]

# Ordenar las puntuaciones con MergeSort
puntuaciones_ordenadas = mergeSort(puntuaciones)

# Obtener las 5 puntuaciones más altas
top_5_puntuaciones = puntuaciones_ordenadas[-5:][::-1]

# Buscar los productos que tengan esas puntuaciones
productos_recomendados = []
for p in productos:
    if p["puntuacion"] in top_5_puntuaciones and p not in productos_recomendados:
        productos_recomendados.append(p)
    if len(productos_recomendados) == 5:
        break

# ------------------ MOSTRAR RECOMENDACIONES ------------------
print("=== SISTEMA DE RECOMENDACIÓN DE PRODUCTOS ===\n")
for prod in productos_recomendados:
    print(f"{prod['nombre']} - Puntuación: {prod['puntuacion']}")
