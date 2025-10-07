aves = list(map(int,input("Ingrese el tipo de ave observada (separados por espacios)")))

id = [0, 0, 0, 0, 0, 0]

for ave in aves:
    conteo[ave] = conteo[ave] + 1

mayor_numero = 0
mas_comun = 0

for i in range(1,6):
    if conteo[i] > mayor_numero:
        mayor_numero = conteo[i]
        mas_comun = i

    print(f"El tipo de ave más común es: {mas_comun}")

