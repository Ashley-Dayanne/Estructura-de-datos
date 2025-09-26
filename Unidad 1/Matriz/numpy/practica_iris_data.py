# Práctica con dataset iris
import numpy as np

# Cargar el dataset
datos=np.genfromtxt('C:/Users/Joshua/Documents/Ashley/Tercero/Estructura de datos/Unidad 1/Matriz/numpy',
                    delimiter=',', dtype='object')

# Visualizar los datos
print(datos)

# Cargar solo las 4 primeras columnas
datos_numericos = np.genfromtxt('C:/Users/Joshua/Documents/Ashley/Tercero/Estructura de datos/Unidad 1/Matriz/numpy',
                                delimiter=',', usecols=(0,1,2,3))

# Visualizar los datos numéricos
print(datos_numericos)

# Listado de índices a eliminar
indices_eliminar=[0,1,2,50]

# Eliminar las filas con los índices detectados con error
datos_limpios=np.delete(datos_numericos, indices_eliminar, axis=0)
print("--------------------- Datos limpios -----------------------", datos_limpios)

datos_limpios[0,0]=np.nan
datos_limpios[4,0]=np.nan
datos_limpios[12,1]=np.nan
datos_limpios[10,2]=np.nan
datos_limpios[10,0]=np.nan
datos_limpios[3,1]=np.nan
datos_limpios[10,2]=np.nan
datos_limpios[4,1]=np.nan
datos_limpios[5,0]=np.nan
datos_limpios[25,1]=np.nan

ultimaFila=datos_limpios.shape[0] - 1
print("Ultima fila: ",ultimaFila)

# Matriz con datos faltantes
print("----------------- Datos con faltantes ---------------------",datos_limpios)

media_columna=np.nanmean(datos_limpios,axis=0)
print("------------- Media de cada columna -------------", media_columna)

# Llenar los valores donde se encuentra nan, por el promedio de cada columna
for i in range(datos_limpios.shape[0]): #shape[0]=filas
    for j in range(datos_limpios.shape[1]): #shape[1]=columnas
        if np.isnan(datos_limpios[i,j]):
            datos_limpios[i,j] = media_columna[j]
print("------------------ Datos sin errores y con nan reemplazados",datos_limpios)
