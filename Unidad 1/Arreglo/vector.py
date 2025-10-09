# Manipulación de un vector de características
''' Problema: Crea un arreglo que represente un vector de características de un objeto (ej. Altura, peso, edad)
    Objetivo: Permite al usuario acceder a un elemento específico por su índice, modificar su valor y calcular la media de todos los elementos '''

persona = [1.75, 70, 25]

print("Altura:",persona[0]," ", "Peso:", persona[1]," ", "Edad:", persona[2])

#modificar los valores
persona[1] = 72
print("peso modificado:", persona[1])

#calcularla media de los datos
media = sum(persona)/len(persona)
print("Media:", media)
