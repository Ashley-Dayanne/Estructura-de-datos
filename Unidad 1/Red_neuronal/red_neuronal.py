# Entrenamiento de una red neuronal

entrada = [1, 2, 3]

# Matriz pesos 3x2
pesos = [
    [4, 1],
    [6, 3],
    [4, 2]
]

salida = [0, 0]

for j in range(len(pesos[0])):
    for i in range(len(entrada)):
        salida[j] += entrada[i] * pesos[i][j]

print("Matriz Entrada", entrada)
print("Matriz pesos", pesos)
print("Matriz salida", salida)
