import numpy as np 

# Creación de una matriz
matriz_A = np.array([
[1,2,3],
[4,5,6],
[7,8,9]
])

# Imprimir matriz original
for fila in matriz_A:
    for elemento in fila:
        print(elemento, end=" ")
    print(" ")

# Acceder a un elemento
elemento = matriz_A[1,2]
print(elemento)

# Modificar un elemento
matriz_A[0,0] = 99

for fila in matriz_A:
    for elemento in fila:
        print(elemento, end=" ")
    print(" ")