estudiantes =[
    (4,2,[-2, 3, -5, 2])
]

print("---------------- Resultados Angry Professor --------------")
for estudiante, rango, tiempos in estudiantes:
    puntuales = 0
    impuntuales = 0
    for x in tiempos:
        if x >= 0:
            puntuales += 1
        else:
            impuntuales += 1

print(f"Total de estudiantes: {estudiante} \n Puntuales: {puntuales} \n Llegaron tarde: {impuntuales} \n Rango: {rango}")

if puntuales < rango:
    print("Resultado: YES (clase cancelada)")
else:
    print("Resultado: NO (clase no cancelada)")
