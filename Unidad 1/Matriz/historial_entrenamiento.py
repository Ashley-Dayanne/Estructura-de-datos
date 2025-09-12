# Historial de entrenamiento de un módelo

precisiones = []

precision = int(input("Ingresa la precisión de cada época (ingresa un número negativo para salir): "))

while precision >= 0:
    precisiones.append(precision)
    precision = int(input("Ingresa la precisión de cada época (ingresa un número negativo para salir): "))

if len(precisiones) > 0:
    precision_final = precisiones[-1]
    precision_maxima = max(precisiones)

    print("Precisión final: ", precision_final, "\n Precisión máxima: ", precision_maxima)

else:
    print("No se ingresó ningún valor.")
