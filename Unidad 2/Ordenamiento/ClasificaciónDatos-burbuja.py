def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  # Intercambio
    return lista


# Ejemplo:
puntajes = [0.8, 0.2, 0.95, 0.6, 0.1]
resultado = burbuja(puntajes)

print("Puntajes ordenados:", resultado)
