import numpy as np

# Ingresar el tamaño de la matriz, sólo es necesario pedir uno, ya que el número de filas y columnas debe ser el mismo
n = int(input("Ingresa el tamaño de la matriz (n): "))

# Crear una matriz aleatoria del tamaño dado con enteros entre -100 y 100
matriz = np.random.randint(-100, 101, size=(n, n))

print("\nMatriz generada:")
print(matriz)

''' Ejempo del documento para confirmar funcionamiento del código:
matriz=[
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
] 
'''

# Calcular las sumas de las diagonales
suma_principal = 0
suma_secundaria = 0

for i in range(n):
    suma_principal += matriz[i][i]           # Diagonal principal
    suma_secundaria += matriz[i][n - 1 - i]  # Diagonal secundaria

# Calcular la diferencia y convertir al valor absoluto
diferencia = suma_principal - suma_secundaria
if diferencia < 0:
    diferencia = -diferencia

print("\nSuma diagonal principal:", suma_principal)
print("Suma diagonal secundaria:", suma_secundaria)
print("Diferencia de las diagonales:", diferencia)

