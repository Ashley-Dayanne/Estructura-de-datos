''' Ejercicio: Detección de colores en una imagen
 Objetivo: Este ejercicio combina conceptos de arreglos, matrices y búsqueda lineal en un escenario de inteligencia artificial '''

 #Pixeles: Rojo = [255,0,0], Verde = [0,255,0], Azul = [0,0,255]

 Imagen= [
    [[0,255,0], [255,0,0], [0,0,255]],
    [[255,0,0], [0,255,0], [255,0,0]],
    [[0,0,255], [255,0,0], [0,255,0]]
 ] 
#Para contar la cantidad de pixeles
color = [0,255,0]
pixeles = 0

for fila in imagen:
    for pixel in fila:
        if pixel == color:
            pixeles += 1

print("Cantidad de pixeles [0,255,0]: ", pixeles)