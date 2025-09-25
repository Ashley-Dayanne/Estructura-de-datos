# Limpieza de datos para Machine Learning
''' Objetivo: 
    Crear una matriz NumPy que represente un conjunto de datos.
    Luego, utilizar una operación de NumPy para eliminar la columna completa que consideres irrelevante.
    Finalmente, imprime la nueva matriz para mostrar que los datos han sido limpiados. '''

import numpy as np

# 1. Crear una matriz NumPy que represente un conjunto de datos
np.random.seed(42)
datos = np.random.rand(5, 9) * 100

print("---------- Datos originales ---------- ")
print(datos)

# Utilizar una operación para eliminar una columna
datos_limpios = np.delete(datos, 4, axis=1) # axis=1 indica que se debe eliminar una columna 
print("\n---------- Datos limpios ---------- ")
print(datos_limpios)