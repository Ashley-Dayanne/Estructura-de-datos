# Tablero de juego con matriz

tablero = [
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 1, 1]
    ]

# Mostrar el tablero en forma de matriz
print(f"Tablero del juego: {tablero}")

# Contar cuántos obstáculos hay en total
obstaculos = 0
for fila in tablero:
    for i in fila:
        if i == 1:
            obstaculos += 1
print(f"En el tablero existen {obstaculos} obstáculos")

# Contar cuántos obstáculos hay en una fila en especifico

fila_elegida = int(input("Ingrese el número de la fila que desea contar (0-4)"))
obstaculos_fila = 0
for i in tablero[fila_elegida]:
    if i == 1:
        obstaculos_fila += 1
print(f"En la fila {fila_elegida} existen {obstaculos_fila} obstáculos")
