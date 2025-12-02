def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio  # Se encontró el valor
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1  # No encontrado


# Ejemplo de uso:
hiperparametros = [0.0001, 0.001, 0.005, 0.01, 0.05, 0.1]
valor_buscado = 0.01

resultado = busqueda_binaria(hiperparametros, valor_buscado)

print("Resultado:", resultado)
