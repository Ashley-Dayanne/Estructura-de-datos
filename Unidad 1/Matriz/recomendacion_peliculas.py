# Ejercicio 5: Sistema de recomendación de películas con matrices
matriz = [
 
    [5,	5,	4,	5,	5,	1,	5,	5,	3,	5,	3,	4,	4],
    [2,	5,	4,	5,	5,	3,	5,	4,	5,	5,	3,	5,	3],
    [2,	5,	5,	5,	4,	3,	5,	4,	4,	5,	2,	4,	3],
    [4,	5,	4,	5,	5,	4,	4,	5,	5,	5,	3,	4,	2],
    [5,	4,	4,	5,	5,	4,	5,	5,	3,	5,	1,	5,	1],
    [3,	5,	3,	5,	3,	5,	2,	1,	3,	5,	3,	1,	1],
    [2,	4,	5,	3,	5,	2,	5,	3,	3,	4,	1,	3,	2],
    [4,	5,	5,	2,	5,	1,	3,	5,	5,	4,	3,	1,	3],
    [3,	2,	5,	2,	5,	2,	3,	2,	5,	4,	5,	4,	2],
    [3,	5,	2,	5,	3,	1,	1,	5,	1,	5,	3,	1,	5],
    [5,	1,	5,	5,	5,	4,	4,	1,	4,	5,	4,	1,	5],
    [5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5],
    [5,	4,	3,	5,	5,	1,	4,	2,	3,	5,	2,	1,	5]
]
 
 #Imprimir la matriz de calificaciones
for i in range(len(matriz)):
    for j in range (len(matriz[i])):
        print(matriz[i][j], end="\t")
    print()

#Calificacion de una pelicula
suma = 0
pelicula = 10

for i in range(len(matriz)):
    suma += matriz[i][pelicula]
print("la suma de calificaciones película es: ", suma)
promedio = suma/ len(matriz)
print("El promedio de calificaciones es: ", promedio)

calificacionesUsuario = matriz[0]
print("Calificaciones del usuario 0: ", calificacionesUsuario)

#Agregar una lógica para que el código pueda leer un arreglo de arreglos y lanzar las calificaciones una por una