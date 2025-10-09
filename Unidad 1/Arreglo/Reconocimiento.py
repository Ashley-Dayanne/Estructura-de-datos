# Reconocimiento de patrones

caracteristicas = [3.5, 1.4, 0.2]

suma = 0
for i in caracteristicas:
    suma += i
print("La suma de las características es: ", suma)

for i in range(len(caracteristicas)):
    caracteristicas[i] = caracteristicas[i]/suma # Normalización
print("Las características normalizadas son: ", caracteristicas)
