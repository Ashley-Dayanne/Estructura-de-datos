import numpy as np

# Creación de una matriz
matriz_A = np.array([
[1,2,3],
[4,5,6],
[7,8,9]
])

for fila in matriz_A:
    for elemento in fila:
        print(elemento, end=" ")
    print()
print("*****************")

# Crear una matriz de ceros
matriz_B = np.zeros((2,3))

for fila in matriz_B:
    for elemento in fila:
        print(elemento, end=" ")
    print()