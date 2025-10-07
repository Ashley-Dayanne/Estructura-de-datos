# Calificaciones de Estudiantes con Matriz y Vectores

calificaciones = []
# Ingresar cantidad de estudiantes
n = int(input("Ingrese el número de estudiantes: "))

# Crear la matriz de calificaciones

for i in range(n):
    fila = []
    print(f"Estudiante {i+1}:")
    for j in range (3):
        calificacion = float(input(f"Ingrese la calificación del examen {j+1}: "))
        fila.append(calificacion)
    calificaciones.append(fila)


# Mostrar matriz de calificaciones
print("\nMatriz de calificaciones:")
print(calificaciones)

# Calcular y mostrar el promedio de cada estudiante
promedios = []
for fila in calificaciones:
    promedio = sum(fila) / len(fila)
    promedios.append(promedio)

print("\nPromedio de cada estudiante:")
for i in range(len(promedios)):
    print(f"Estudiante {i+1}: {promedios[i]:.2f}")

# Calcular promedio de cada examen (columna)
promedio_examenes = []
for j in range(3):
    suma = 0
    for i in range(n):
        suma += calificaciones[i][j]
    promedio = suma / n
    promedio_examenes.append(promedio)

print("\nPromedio de cada examen:")
for j in range(3):
    print(f"Examen {j+1}: {promedio_examenes[j]:.2f}")

# Determinar qué estudiante obtuvo la calificación más alta en el curso
max_nota = 0
estudiante_max = 0
for i in range(n):
    for j in range(3):
        if calificaciones[i][j] > max_nota:
            max_nota = calificaciones[i][j]
            estudiante_max = i + 1  # +1 para mostrar en base 1

print(f"\nEl estudiante {estudiante_max} obtuvo la calificación: {max_nota}, siendo esta la más alta del curso")

